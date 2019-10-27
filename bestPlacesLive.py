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
driver.get("https://www.niche.com/places-to-live/search/safest-neighborhoods/")

csv_file = open('bestPlacesLive_data_4.csv', 'w', encoding='utf-8', newline='')
writer=csv.writer(csv_file)

page=1
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
                time.sleep(3)
                #Loops through the xpath, {} is where the .format(i) will input it's value
                #get national ranking for best neighborhoods in America
                # ranking_link='//li[@class="search-results__list__item"][{}]/div/div/a/div[2]/div'.format(i)
                # isPresent=driver.find_element_by_xpath(ranking_link)
                #
                # if bool(isPresent)==False:
                #     ranking=' '
                #     final_data_dict['ranking']=ranking
                #     print("not present")
                #
                # if bool(isPresent)==True:
                #     ranking=driver.find_element_by_xpath(ranking_link).text
                #     final_data_dict['ranking']=ranking
                #     print("it is present")

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
                #check if state ranking exists
                # try:
                #     if bool(driver.find_element_by_xpath('//div[@class="postcard__content-container"]/div[2]/div[1]/div[2]/a')==True):
                #         state_ranking=driver.find_element_by_xpath('//div[@class="postcard__content-container"]/div[2]/div[1]/div[2]/a').text
                #         final_data_dict['state_ranking']=state_ranking
                #         print('state_ranking %s' %state_ranking)
                #     if bool(driver.find_element_by_xpath('//div[@class="postcard__content-container"]/div[2]/div[1]/div[2]/a')==False):
                #         state_ranking=' '
                #         final_data_dict['state_ranking']=state_ranking
                #         pass
                # except:
                #     continue

                state=driver.find_element_by_xpath('//ul[@class="profile-breadcrumbs"]/li[1]').text
                print('state %s' %state)
                city=driver.find_element_by_xpath('//ul[@class="profile-breadcrumbs"]/li[2]').text
                print('city %s' %city)
                neighborhood=driver.find_element_by_xpath('//h1[@class="postcard__title"]').text
                print('neighborhood %s' %neighborhood)
                niche_grade=driver.find_element_by_xpath('//div[@class="overall-grade__niche-grade"]').text
                print('niche_grade %s' %niche_grade)
                public_schools=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][1]/div/div[2]').text
                print('public_schools %s' %public_schools)
                crime_and_safety=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][2]/div/div[2]').text
                print('crime_and_safety %s' %crime_and_safety)
                housing=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][3]/div/div[2]').text
                print('housing %s' %housing)
                nightlife=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][4]/div/div[2]').text
                print('nightlife %s' %nightlife)
                good_for_families=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][5]/div/div[2]').text
                print('good_for_families %s' %good_for_families)
                diversity=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][6]/div/div[2]').text
                print('diversity %s' %diversity)
                jobs=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][7]/div/div[2]').text
                print('jobs %s' %jobs)
                weather=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][8]/div/div[2]').text
                print('weather %s' %weather)
                cost_of_living=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][9]/div/div[2]').text
                print('cost_of_living %s' %cost_of_living)
                health_and_fitnes=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][10]/div/div[2]').text
                print('health_and_fitnes %s' %health_and_fitnes)
                outdoor_activities=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][11]/div/div[2]').text
                print('outdoor_activities %s' %outdoor_activities)
                commute=driver.find_element_by_xpath('//li[@class="ordered__list__bucket__item"][12]/div/div[2]').text
                print('commute %s' %commute)
                population=driver.find_element_by_xpath('//section[@class="block--two"]/div[2]/div[1]/div/div/div[2]/div[2]').text
                print('population %s' %population)
                area_feel=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[2]/div/div/div[1]/div[2]').text
                print('area_feel %s' %area_feel)
                #changed xpath
                median_home_value=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[1]/div/div/div[1]/div[2]').text
                print('median_home_value %s' %median_home_value)
                #changed xpath
                median_rent=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[1]/div/div/div[2]/div[2]').text
                print('median_rent %s' %median_rent)
                people_rent_percentage=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[1]/div[3]').text
                print('people_rent_percentage %s' %people_rent_percentage)
                people_own_percentage=driver.find_element_by_xpath('//section[@class="block--two-one"]/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[2]/div[3]').text
                print('people_own_percentage %s' %people_own_percentage)
                median_household_income=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[2]/div/div/div[1]/div[2]/span').text
                print('median_household_income %s' %median_household_income)
                families_children=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[2]/div/div/div[2]/div[2]/span').text
                print('families_children %s' %families_children)
                masters_degree=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[3]/div/div/div/div[2]/ul/li[1]/div[3]').text
                print('masters_degree %s' %masters_degree)
                bachelors_degree=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[3]/div/div/div/div[2]/ul/li[2]/div[3]').text
                print('bachelors_degree %s' %bachelors_degree)
                associate_degree=driver.find_element_by_xpath('//section[@class="block--one-two"]/div[2]/div[3]/div/div/div/div[2]/ul/li[3]/div[3]').text
                print('associate_degree %s' %associate_degree)


                final_data_dict['state']=state
                final_data_dict['city']=city
                final_data_dict['neighborhood']=neighborhood
                final_data_dict['niche_grade']=niche_grade
                final_data_dict['public_schools']=public_schools
                final_data_dict['crime_and_safety']=crime_and_safety
                final_data_dict['housing']=housing
                final_data_dict['nightlife']=nightlife
                final_data_dict['good_for_families']=good_for_families
                final_data_dict['diversity']=diversity
                final_data_dict['jobs']=jobs
                final_data_dict['weather']=weather
                final_data_dict['cost_of_living']=cost_of_living
                final_data_dict['health_and_fitnes']=health_and_fitnes
                final_data_dict['outdoor_activities']=outdoor_activities
                final_data_dict['commute']=commute
                final_data_dict['population']=population
                final_data_dict['area_feel']=area_feel
                final_data_dict['median_home_value']=median_home_value
                final_data_dict['median_rent']=median_rent
                final_data_dict['people_rent_percentage']=people_rent_percentage
                final_data_dict['people_own_percentage']=people_own_percentage
                final_data_dict['median_household_income']=median_household_income
                final_data_dict['families_children']=families_children
                final_data_dict['masters_degree']=masters_degree
                final_data_dict['bachelors_degree']=bachelors_degree
                final_data_dict['associate_degree']=associate_degree

                writer.writerow(final_data_dict.values())

                #sleep 1 second before leaving the website
                time.sleep(1)
                #goes back to the main page
                driver.back()
            except:
                continue

        next_button=driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/section/div[3]/section/div/ul/li[3]')
        next_button.click()
        time.sleep(3)

    except:
        print('Exit')
        #closes csv file
        csv_file.close()
        #closes driver
        driver.close()
        break
