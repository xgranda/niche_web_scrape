from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome()

#driver for main website
driver.get("https://www.niche.com/places-to-live/search/safest-neighborhoods/?page=31")

csv_file = open('bestPlacesLive_data_3.csv', 'w', encoding='utf-8', newline='')
writer=csv.writer(csv_file)

page=31
while True:
    try:
        print("Scraping Page number %s" %page)
        page = page + 1
        # loops through each neighborhood in the page
        for i in range(1,34):
            try:
                #Initialize empty dictionary to store data
                final_data_dict={}
                #sleep 5 seconds
                time.sleep(5)
                #Loops through the xpath, {} is where the .format(i) will input it's value
                #get national ranking for best neighborhoods in America
                ranking_link='//li[@class="search-results__list__item"][{}]/div/div/a/div[2]/div'.format(i)
                ranking=driver.find_element_by_xpath(ranking_link).text
                # Look for information inside neighborhood link
                p1='//li[@class="search-results__list__item"][{}]/div/div/a'.format(i)
                #clicks on every link
                city_button = driver.find_element_by_xpath(p1)

                # Click button to go to each neighborhood
                city_button.click()

                #Click on expand values to check retrieve more information
                info_button = driver.find_element_by_xpath('//a[@class="report-card__toggle"]')
                info_button.click()

                #XPATH's are that long because they share the same classes in different blocks of the code
                #I had to get the XPATH from different parts of the same block to see where the code separated
                state_ranking=driver.find_element_by_xpath('//div[@class="postcard__content-container"]/div[2]/div[1]/div[2]/a').text
                state=driver.find_element_by_xpath('//ul[@class="profile-breadcrumbs"]/li[1]').text
                city=driver.find_element_by_xpath('//ul[@class="profile-breadcrumbs"]/li[2]').text
                neighborhood=driver.find_element_by_xpath('//h1[@class="postcard__title"]').text
                niche_grade=driver.find_element_by_xpath('//div[@class="overall-grade__niche-grade"]').text
                public_schools=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][1]/div/div[2]').text
                crime_and_safety=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][2]/div/div[2]').text
                housing=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][3]/div/div[2]').text
                nightlife=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][4]/div/div[2]').text
                good_for_families=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][5]/div/div[2]').text
                diversity=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][6]/div/div[2]').text
                jobs=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][7]/div/div[2]').text
                weather=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][8]/div/div[2]').text
                cost_of_living=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][9]/div/div[2]').text
                health_and_fitnes=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][10]/div/div[2]').text
                outdoor_activities=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][11]/div/div[2]').text
                commute=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][12]/div/div[2]').text
                population=driver.find_element_by_xpath('//section[@class="block--two"]/div[2]/div[1]/div/div/div[2]/div[2]').text
                area_feel=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[2]/div/div/div[1]/div[2]').text
                median_home_value=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[1]/div/div/div[1]/div[2]/span').text
                median_rent=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[1]/div/div/div[2]/div[2]/span').text
                people_rent_percentage=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[1]/div[3]').text
                people_own_percentage=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[2]/div[3]').text
                median_household_income=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[2]/div/div/div[1]/div[2]/span').text
                families_children=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[2]/div/div/div[2]/div[2]/span').text
                masters_degree=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[3]/div/div/div/div[2]/ul/li[1]/div[3]').text
                bachelors_degree=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[3]/div/div/div/div[2]/ul/li[2]/div[3]').text
                associate_degree=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[3]/div/div/div/div[2]/ul/li[3]/div[3]').text


                    # final_data_dict['ranking']=ranking
                    # final_data_dict['state_ranking']=state_ranking
                    # final_data_dict['state']=state
                    # final_data_dict['city']=city
                    # final_data_dict['neighborhood']=neighborhood
                    # final_data_dict['niche_grade']=niche_grade
                    # final_data_dict['public_schools']=public_schools
                    # final_data_dict['crime_and_safety']=crime_and_safety
                    # final_data_dict['housing']=housing
                    # final_data_dict['nightlife']=nightlife
                    # final_data_dict['good_for_families']=good_for_families
                    # final_data_dict['diversity']=diversity
                    # final_data_dict['jobs']=jobs
                    # final_data_dict['weather']=weather
                    # final_data_dict['cost_of_living']=cost_of_living
                    # final_data_dict['health_and_fitnes']=health_and_fitnes
                    # final_data_dict['outdoor_activities']=outdoor_activities
                    # final_data_dict['commute']=commute
                    # final_data_dict['population']=population
                    # final_data_dict['area_feel']=area_feel
                    # final_data_dict['median_home_value']=median_home_value
                    # final_data_dict['median_rent']=median_rent
                    # final_data_dict['people_rent_percentage']=people_rent_percentage
                    # final_data_dict['people_own_percentage']=people_own_percentage
                    # final_data_dict['median_household_income']=median_household_income
                    # final_data_dict['families_children']=families_children
                    # final_data_dict['masters_degree']=masters_degree
                    # final_data_dict['bachelors_degree']=bachelors_degree
                    # final_data_dict['associate_degree']=associate_degree

                writer.writerow(final_data_dict.values())

                #sleep 1 second before leaving the website
                time.sleep(1)
                #goes back to the main page
                driver.back()

            except:
                continue
            print('ranking %s' %ranking)
            print('state_ranking %s' %state_ranking)
            print('state %s' %state)
            print('city %s' %city)
            print('neighborhood %s' %neighborhood)
            print('niche_grade %s' %niche_grade)
            print('public_schools %s' %public_schools)
            print('crime_and_safety %s' %crime_and_safety)
            print('housing %s' %housing)
            print('nightlife %s' %nightlife)
            print('good_for_families %s' %good_for_families)
            print('diversity %s' %diversity)
            print('jobs %s' %jobs)
            print('weather %s' %weather)
            print('cost_of_living %s' %cost_of_living)
            print('health_and_fitnes %s' %health_and_fitnes)
            print('outdoor_activities %s' %outdoor_activities)
            print('commute %s' %commute)
            print('population %s' %population)
            print('area_feel %s' %area_feel)
            print('median_home_value %s' %median_home_value)
            print('median_rent %s' %median_rent)
            print('people_rent_percentage %s' %people_rent_percentage)
            print('people_own_percentage %s' %people_own_percentage)
            print('median_household_income %s' %median_household_income)
            print('families_children %s' %families_children)
            print('masters_degree %s' %masters_degree)
            print('bachelors_degree %s' %bachelors_degree)
            print('associate_degree %s' %associate_degree)

        next_button=driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/section/div[3]/section/div/ul/li[3]')
        next_button.click()
        time.sleep(4)

    except:
        print('Exit')
        #closes csv file
        csv_file.close()
        #closes driver
        driver.close()
        break
