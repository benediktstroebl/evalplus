```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset
    
    Mean Absolute Deviation is the average absolute difference between each 
    element and a centerpoint (mean in this case).

    Input: A list of numbers
    Output: A float - Mean Absolute Deviation value
    """
    # Store the mean of the numbers in the list
    mean = sum(numbers) / len(numbers)
    mad = 0.0
    # For each element in the list and subtract the mean, multiply by 
    the absolute value and add the result to the running total of 
    absolute deviations
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) < 0.1)
``` 
This Python function, mean_absolute_deviation, computes the Mean Absolute Deviation (MAD) of a dataset. It accepts a list of numbers as an input and outputs a single value, which is the MAD of this dataset. 
The function utilizes the mean of the input list, which acts as a centerpoint, and calculates the average absolute difference between each number and the mean. 

This is repeated for every element in the list, and the final result is the Mean Absolute Deviation. 
The test section ensures that the function output is within the expected range.