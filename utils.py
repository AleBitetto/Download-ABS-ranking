import zipfile
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service




def get_chromedriver(chromedriver_path=None, use_proxy=False, user_agent=None,
                    PROXY_HOST=None, PROXY_PORT=None, PROXY_USER=None, PROXY_PASS=None, download_folder=None,
                    desired_capabilities=None, return_options_only=False):

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

    chrome_options = webdriver.ChromeOptions()
    # allow multiple download
    prefs_experim = {'profile.default_content_setting_values.automatic_downloads': 1}
    
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    if download_folder:
        prefs_experim["download.default_directory"] = download_folder

    chrome_options.add_experimental_option("prefs", prefs_experim)

    if return_options_only:
        return chrome_options
    else:
        driver = webdriver.Chrome(
            service=Service(chromedriver_path), # executable_path=chromedriver_path,
            options=chrome_options,
            desired_capabilities=desired_capabilities)
        
        return driver