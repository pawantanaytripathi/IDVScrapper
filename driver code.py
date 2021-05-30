import time
import csv
import pandas
from os import path
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


def setAttributes(url, month, year, vehicleType, driverPath):

	driver = webdriver.Chrome(executable_path = driverPath)
	driver.get(url)

	elementVehicle = driver.find_element_by_name("vehicletype")
	elementMonth = driver.find_element_by_name("month")
	elementYear = driver.find_element_by_name("year")

	# using select method to perform other operations
	temp1 = Select(elementVehicle)
	temp2 = Select(elementMonth)
	temp3 = Select(elementYear)

	# selecting the Two Wheeler as per required
	temp1.select_by_visible_text(vehicleType)
	temp3.select_by_visible_text(year)

	# adding exteranl wait so that march is shown for year 2021
	time.sleep(1)
	temp2.select_by_visible_text(month)

	driverMain(driver)

	return True


def driverMain(driver):

	
	i = 2                                                                      # setting wait time
	final = []
	makeModelDict = {}

	elementState = driver.find_element_by_name("city")
	elementMake = driver.find_element_by_name("make")
	elementModel = driver.find_element_by_name("model")
	elementVariant = driver.find_element_by_name("variant")
	temp5 = Select(elementState)
	temp6 = Select(elementMake)
	temp7 = Select(elementModel)
	temp8 = Select(elementVariant)
	Flag1 = False

	for state in elementState.find_elements_by_tag_name("option"):

		if Flag1 == False:
			Flag1 = True
			continue

		temp5.select_by_visible_text(state.get_attribute("text"))
		Flag2 = False

		for make in elementMake.find_elements_by_tag_name("option"):

			temp6.select_by_visible_text(make.get_attribute("text"))
			time.sleep(i)
			Flag3 = False

			for model in elementModel.find_elements_by_tag_name("option"):
				if Flag3 == False:
					Flag3 = True
					continue

				temp7.select_by_visible_text(model.get_attribute("text"))
				time.sleep(i/2)
				Flag4 = 0

				for variant in elementVariant.find_elements_by_tag_name("option"):
					if Flag4 == False:
						Flag4 = True
						continue

					temp8.select_by_visible_text(variant.get_attribute("text"))
				
					button = driver.find_element_by_id("showPrice")
					button.click()
					time.sleep(i)

					pricing = driver.find_element_by_id("price").text

					final.append([state.text, make.text, model.text, variant.text, pricing])

					writeToCsv(final)
		
	return True


def writeToCsv(final):

	# Writes each record to csv file 

    if path.exists("records.csv") == False:
                
        with open('records.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["State", "Make", "Model", "Variant", "IDV Value", "Year", "Month", "Vehicle Type"])
           
            for i in final:
            	writer.writerow(i)

            file.close()
            
    else:
        with open('records.csv', 'a', newline = '') as file:
            writer = csv.writer(file)

            for i in final:
            	writer.writerow(i)

            file.close()
            
    # Drop rows with any empty cells
    df = pandas.read_csv('records.csv')
    df['Year'] = "2021"
    df['Month'] = "March"
    df['Vehicle Type'] = "Two Wheeler"
    df.to_csv('records.csv', index=False)
    df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

    return True

































