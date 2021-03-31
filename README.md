# Linkedin Jobs

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



