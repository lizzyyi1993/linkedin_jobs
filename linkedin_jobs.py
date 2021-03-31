import pandas as pd
from pandas.core.frame import DataFrame
import re
import codecs
import pymysql
pymysql.install_as_MySQLdb()
import warnings
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from time import time
start_time = time()

from warnings import warn

# replace variables here.
urls = ["https://www.linkedin.com/jobs/search/?f_L=San%20Francisco%20Bay%20Area&f_TPR=r604800&geoId=90000084&keywords=data%20scientist&location=San%20Francisco%20Bay%20Area&sortBy=DD",
"https://www.linkedin.com/jobs/search/?f_L=Austin%2C%20Texas%20Metropolitan%20Area&f_TPR=r604800&geoId=90000064&keywords=data%20scientist&location=Austin%2C%20Texas%20Metropolitan%20Area&sortBy=DD",
"https://www.linkedin.com/jobs/search/?geoId=105080838&keywords=data%20scientist&location=New%20York%2C%20United%20States",
"https://www.linkedin.com/jobs/search/?geoId=104116203&keywords=data%20scientist&location=Seattle%2C%20Washington%2C%20United%20States"]


SQL_DB = "Linkedin"
# Need to replace with your own password
conn = pymysql.connect(host='localhost', user = 'root', password = '')
cursor = conn.cursor()

query = "CREATE DATABASE IF NOT EXISTS " + SQL_DB
cursor.execute(query);

k = 1
for url in urls:
    driver = webdriver.Chrome("/Users/lizzy929/Desktop/BAX 452 ML/final project/chromedriver")
    driver.get(url)
    sleep(10)
    action = ActionChains(driver)
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        sleep(3)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break 


    # parsing the visible webpage
    pageSource = driver.page_source
    lxml_soup = BeautifulSoup(pageSource, 'lxml')

    # searching for all job containers
    job_container = lxml_soup.find('ul', class_ = 'jobs-search__results-list')

    print('You are scraping information about {} jobs.'.format(len(job_container)))

    # setting up list for job information
    job_id = []
    post_title = []
    company_name = []
    post_date = []
    job_location = []
    job_desc = []
    level = []
    emp_type = []
    functions = []
    industries = []
    Number_of_applicants = []
    salary = []
    criteria_list = []
    test = []
    link = []

    # for loop for job title, company, id, location and date posted
    for job in job_container:
        
        # job title
        job_titles = job.find("span", class_="screen-reader-text").text
        post_title.append(job_titles)
        
        # linkedin job id
        job_ids = job.find('a', href=True)['href']
        job_ids = re.findall(r'(?!-)([0-9]*)(?=\?)',job_ids)[0]
        job_id.append(job_ids)
        
        # company name
        company_names = job.select_one('img')['alt']
        company_name.append(company_names)
        
        # job location
        job_locations = job.find("span", class_="job-result-card__location").text
        job_location.append(job_locations)
        
        # posting date
        post_dates = job.select_one('time')['datetime']
        post_date.append(post_dates)

    # for loop for job description and criterias
    for x in range(1,len(job_id)+1):
        
        # clicking on different job containers to view information about the job
        job_xpath = '/html/body/main/div/section/ul/li[{}]/img'.format(x)
        driver.find_element_by_xpath(job_xpath).click()
        sleep(3)
        
        # Applicants
        applicants = driver.find_element_by_css_selector('.num-applicants__caption').text.split(' ')
        if len(applicants) > 2:
            Number_of_applicants.append(applicants[-2])
        else:
            Number_of_applicants.append(applicants[0])
        
        # Salary
        try:
            salaries = driver.find_element_by_css_selector('.compensation__salary').text 
            salary.append(salaries)
        except Exception as ex:
            salary.append("null")
            
        # Link
        links = driver.find_element_by_css_selector('div.topcard__content-left > a').get_attribute('href')
        link.append(links)
        
        criteria = driver.find_element_by_css_selector('ul.job-criteria__list').text
        criteria_list.append(criteria)
        p = criteria_list[x-1]
        p2 = p.split("\n")

        # job description
        try:
            xpath = '/html/body/main/section/div[2]/section[2]/div/section/button[1]'
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            sleep(5)
            job_descs = driver.find_element_by_css_selector('.description__text--rich').text
            job_desc.append(job_descs)
        except Exception as ex:
            job_descs = driver.find_element_by_css_selector('.description__text--rich').text
            job_desc.append(job_descs)

        try:
            level.append(p2[1])
        except Exception as ex:
            level.append("null")
        
        try:
            emp_type.append(p2[3])
        except Exception as ex:
            emp_type.append("null")
        
        try:
            functions.append(p2[5])
        except Exception as ex:
            functions.append("null")
        
        try:
            industries.append(p2[7])
        except Exception as ex:
            industries.append("null")
        
        
        
        x = x+1

    # to check if we have all information
    print(len(job_id))
    print(len(post_date))
    print(len(company_name))
    print(len(post_title))
    print(len(job_location))
    print(len(job_desc))
    print(len(level))
    print(len(emp_type))
    print(len(functions))
    print(len(industries))
    print(len(salary))
    print(len(Number_of_applicants))
    print(len(link))

    job_data = pd.DataFrame({'Job ID': job_id,
    'Date': post_date,
    'Link': link,
    'Company Name': company_name,
    'Post': post_title,
    'Location': job_location,
    'Description': job_desc,
    'Salary' : salary,
    'Level': level,
    'Type': emp_type,
    'Function': functions,
    'Industry': industries,
    'Applicantes': Number_of_applicants
    })

    # cleaning description column
    job_data['Description'] = job_data['Description'].str.replace('\n',' ')

    print(job_data.info())
    print(job_data.head())

    keywords = ['SQL', 'Tableau', 'Excel', 'Python', 'R', 'JavaScript', 'MongoDB', 'Looker']
    Num = []

    for key in keywords:
        bool = job_data['Description'].str.contains(key)
        Num.append(job_data[bool]['Job ID'].count())
    df = DataFrame({"Skills": keywords, "Number": Num}).sort_values(by='Number', axis = 0, ascending = False)
    print(df)

    #ignore warnings
    warnings.filterwarnings("ignore")
    SQL_TABLE = "Job"+str(k)
    SQL_TABLE_DEF = "(" + \
                "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY" + \
                ",Job_ID int(20)" + \
                ",Date date" + \
                ",Link VARCHAR(300)" + \
                ",Company VARCHAR(100)" + \
                ",Title VARCHAR(50)" + \
                ",Location VARCHAR(100)" + \
                ",Description Text" + \
                ",Salary VARCHAR(50)" + \
                ",Level VARCHAR(50)" + \
                ",Type VARCHAR(50)" + \
                ",Functions VARCHAR(100)" + \
                ",Industry VARCHAR(100)" + \
                ",Applicants int(20)" + \
                ")"

    query = "CREATE TABLE IF NOT EXISTS " + SQL_DB + "." + SQL_TABLE + " " + SQL_TABLE_DEF + ";";
    cursor.execute(query);
    # Need to replace with your own password after root before "@"
    engine =  create_engine('mysql://root:@localhost/Linkedin')


    job_data.to_sql(SQL_TABLE, con = engine, if_exists = 'replace')

    k=k+1

cursor.close()
conn.close()