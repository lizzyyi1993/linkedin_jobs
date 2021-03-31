# Data Analytics Job Postings Analysis

## Overview
The purpose of this project is to explore the data science opportunities in the job market nowadays, help data analytics enthusiasts land their dream jobs in the data analytics
field, and assist companies with talent acquisition as the recruiting season is approaching.
Therefore, we conducted people analytics and compared data science opportunities across different locations, industries and functions on LinkedIn. We used Python to scrape the LinkedIn data analyst job opening data, which was then stored into MySQL database because of its data security, high performance under low cost, and fast speed.

In this way, we were able to retrieve real-time information about data analytics talent acquisition in the job market. Based on the web scraping results, we concluded the following four main insights:
1. The Bay Area, Seattle, and NYC continue to be one of the areas that have most data science opportunities available. The competition in new york city is the most intense compared to the other 3 three areas. Although the job openings are less in Austin, the competition is also low.
2. Tech industry remains to be the most popular industry data analyst candidates would like to work for. Besides the tech industry, finance services and marketing industries are also one of the top 10 popular industries.
3. Python, R and SQL are the top three skills recruiters are looking for in a qualified data analyst candidate.
4. Most of the companies are not willing to disclose the salary level for the job position in public, which gives hired candidates room to negotiate for the salaries. The insights generated from our database can provide business value for both talents and companies, providing candidates with consulting services in the job hunting process and companies with real-time job market information.

## Data Sources
We used Linkedin as our main data source as it is one of the biggest employment oriented online service companies candidates use for job searching in the recruiting season. Specifically, here are the fields we web scrapped and saved to our database:
1. Job id
2. Post date
3. Application link
4. Company name
5. Job title
6. Job location
7. Job description
8. Salary
9. Level
10. Employment type
11. Function
12. Industry
13. Number of applicants

Due to the rising number of data analytics opportunities outside of the bay area, we scrapped the data for the following locations that we believe are data analytics professionals’ population destinations:
1. Bay Area (San Francisco, Mountain View, Menlo Park, San Jose, etc)
2. Seattle
3. Austin
4. New York City

## Web Scraping Steps
1. We imported all the necessary packages for the web scraping. Because of the unique UI design Linkedin job page has, which the jobs are listed on the left side as a float, and we had to click on each job title to see more detailed descriptions. We downloaded the chromedriver in order to automate the navigation of each job posting. Specifically, we got the screen height of the web first, scrolled one screen height each time, then updated scroll height each time after scrolling as the scroll height can change after we scrolled the page, and broke the loop when the height we need to scroll to is larger than the total scroll height. 
2. After that, we parsed the visible webpages, searched for all job containers, and set up the lists for job information such as job id, job title, etc. We located each element by using css selectors and printed them down.
3. To investigate the skills needed as a data analyst, we also looked a little more into the job description. We listed the common skills that recruiters look for in a data analyst such as R, Python, SQL, Java, Excel, Tableau, Looker, MongoDB, etc. For each job description of the job posting, we counted the number of times that appeared in the job description to determine what are the most relevant skills the companies are looking for in a candidate by sorting them in a descending order.

## Dataset & Database Design Choices
The final dataset for each column from left to right are Job id, Post date, Application link, Company name, Job title, Job location, Job description, Salary, Level, Employment type, Function, Industry, Number of applicants.

We chose to store our data into MySQL because of three reasons: 
1. It’s a mature tool and has high performance on a limited budget as we just get started
2. MySQL is the most secure DBMS in the market
3. MySQL has easy and low-maintenance setup, which fits our need since we have a stable schema and don’t need to scale much on our database

## Discoveries & Insights
We compared the number of applicants and the number of data analyst job openings in different dimensions such as state on a real-time basis. We analyzed the job market competitiveness by looking at data analyst openings around these popular cities and spot new opportunities for applicants.

For example, although Austin has been known as the silicon hill and there have been more people who work in tech moving there, data analysts opportunities are still more prevalent in new york city, bay area, and seattle. In addition, New York City seems to have a more fierce competition with 108.68 applicants per job opening. Although there are less available opportunities in Austin, the competition is not as intense as the other 3 cities with only 28.5 applicants per job opening.

Information like this gives us an opportunity to convey this message to applicants and help them spot new opportunities. On the other hand, we can also help companies in those areas market their openings and improve visibility.

We also investigated the popularity of the industries for data analyst candidates and analyzed the number of applicants for each industry. The top 10 industries are mainly in the field such as information technology, internet, software, etc, which are categorized as tech industries. Financial services and marketing industries also attract a decent number of data analyst applicants.

Lastly, we also analyzed the popular computing skills that companies are looking for in candidates by counting the number of times that keywords appeared in the job description. We concluded that R, Python and SQL are the most popular programming languages, which are in line with our expectations.
