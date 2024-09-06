Here's a solution:

def mean_absolute_deviation(numbers):  
    from statistics import mean  
    numbers.sort()  
    x_mean = mean(numbers)
    mad = sum([x-x_mean for x in numbers]) / len(numbers)  
    return mad 

This solution defines a function `mean_absolute_deviation` which takes a list of numbers as input and returns the Mean Absolute Deviation for the dataset. The Mean Absolute Deviation is a measure of the average absolute difference between each element in the dataset and the mean of the dataset.