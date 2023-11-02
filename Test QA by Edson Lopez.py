"""
Test QA Cart.com by Edson Lopez
Nov 1st 2023
"""

from statistics import median
import datetime

input1 = [1, 5, -2, 8, 0, -2, 5, 1, 10, -5]
input2 = [2.5, 3.5, 1.5, 2.5, 2.5]
input3 = [1, 3.5, "apple", 2.5, 1, 3, "banana"]
input4 = [datetime.date(2022, 1, 1), datetime.date(2021, 1, 1), datetime.date(2022, 1, 1)]
input5 = []

data = input1

def analyze_data(data):
    #The function should ignore non-numeric data. Filter and convert to numeric values (integers and floats).
    numeric_values = [item for item in data if isinstance(item, (int, float))]

    #Find the minimum value in the data.
    min_value = min(numeric_values) if len(numeric_values) > 0 else None
    
    #Find the maximum value in the data.
    max_value = max(numeric_values) if len(numeric_values) > 0 else None

    #Calculate the average value of the data.
    avg_value = sum(numeric_values) / len(numeric_values) if len(numeric_values) > 0 else None

    #Identify the count of unique values in the data.
    unique_values = len(set(numeric_values)) if len(numeric_values) > 0 else 0

    #Determine the median value (the middle value when the data is sorted).
    sorted_numeric_values = sorted(numeric_values)
    median_value = median(sorted_numeric_values) if len(sorted_numeric_values) > 0 else None

    return min_value, max_value, avg_value, unique_values, median_value

min_value, max_value, avg_value, unique_values, median_value = analyze_data(data)

#1)Test with a list of integers containing positive and negative values:
print(analyze_data(input1))
#2)Test with a list of floats:
print(analyze_data(input2))
#3)Test with a list of mixed data types (integers, floats, and strings):
print(analyze_data(input3))
#4)Test with a list of dates (datetime objects):
print(analyze_data(input4))
#5) Test with an empty list:
print(analyze_data(input5))