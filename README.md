# Download ABS ranking
Download [ABS Journal Ranking](https://charteredabs.org/academic-journal-guide-2021-view/)


### Chrome Web Driver

To download data, this notebook relies on [`selenium`](https://selenium-python.readthedocs.io/) and [`ChromeDriver`](https://chromedriver.chromium.org/).

This requires a `chromedriver` executable which can be downloaded [here](https://chromedriver.chromium.org/downloads). Make sure that your `Chrome` version is the same as your `chromedriver` version.

The notebook assumes that the `chromedriver` executable is located at `/WebDriver` in the main folder. To supply a different path, change the variable `chromedriver_path` in the notebook.

### Credentials

Credentials must be inputed manually into a `config.py` file. Create a text file with the following lines:
```
User = "username"
Password = "password"
```
where you need to write the Login credential for the ABS website. Then simply rename the file as `.py`
