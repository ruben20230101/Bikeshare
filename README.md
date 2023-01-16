# Bikeshare: 

As a student taking the Udacity US bike share project, I had the opportunity to explore data from bike share systems in three major cities in the United States: Chicago, New York City, and Washington. The project was divided into several parts and it helped me to learn about data analysis and visualization by diving into the data.

The goal of this project was to design a python script that can be ran in a command line interpreter capable of extracting a specific subset from any of the three given datasets (one per city), based on user-specified parameters: city, month, and day of the week. Addtionally, the script should not crash based on incorrect input, e.g., typos and incorrect capitalization.

As the developer of this code, I created a program that allows users to explore bike share data from three US cities: Chicago, New York City, and Washington. The program starts by importing necessary libraries like time, pandas, and numpy. I defined some global variables such as CITY_DATA, MONTHS, DAYS, and CITIES that contain the name of the cities, months and days respectively.

I created a function called get_filters() that prompts the user to specify the city, month, and day that they want to analyze. It uses a while loop to handle invalid inputs and returns the city, month, and day that the user specifies.

The load_data() function takes the city, month, and day as input and loads the corresponding data file into a dataframe using pandas. It also converts the Start Time column to datetime, extracts month, day of the week and hour from Start Time to create new columns. The function filters by month and day of the week if specified by the user.

The time_stats() function takes the filtered dataframe as input and calculates various statistics such as most common month, day of the week, and hour of the day for the bike rides.

Overall, this code allows users to interactively explore bike share data from different cities and filter by month and day of the week

Sources:

Use of parentheses in load_data chapter:
https://www.delftstack.com/howto/python/python-datetime-day-of-week/

How to find the most common value (mode):
https://www.geeksforgeeks.org/python-statistics-mode-function/

Month name to month number:
https://www.studytonight.com/python-howtos/how-to-get-month-name-from-month-number-in-python

Weekday error:
https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week

Capitalization of day of the week:
https://www.w3schools.com/python/ref_string_capitalize.asp

Sources used for combination of start and end station function:
https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/
https://www.geeksforgeeks.org/numpy-size-function-python/
https://www.tutorialspoint.com/python-sort-grouped-pandas-dataframe-by-group-size
