# Insured Declared Value Scrapper

A python script based on selenium which scraps all the IDV values from the site: https://idv.gicouncil.in/

## Features
- Scrap all values for any state or any particular brand of vehicle.
- Selenium based script so the scrapping is completely automated just download the chrome driver to work with it.
- The script dumps all the data in the records.csv, a sample records.csv is present in the project directory for you to check the formatting.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies-

```bash
pip install selenium
```

```bash
Download the chrome webdriver here - 
https://chromedriver.chromium.org/downloads
```

## Usage

```bash
Simply clone the repository in your system & run the main.py to start scrapping.
To make changes to the script just open driver code.py

NOTE: The script is a bit slow as the selenium itself is not the most time saving
way of scrapping but it gets the job done.

```

Please make sure to install other latest libraries as per your need.

## License
[MIT](https://choosealicense.com/licenses/mit/)
