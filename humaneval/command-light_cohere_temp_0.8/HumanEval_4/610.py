Here's the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Mean Absolute Deviation
    Calculate the mean of the numbers in the list and then calculate the absolute deviation of each number with the mean.
    Return the mean absolute deviation as a single value
    """
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Test cases 
numbers1 = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers1)
print(result) 

numbers2 = [1.0, 2.0, 3.0]
result = mean_absolute_deviation(numbers2)
print(result) 

numbers3 = [0.5, 0.5, 0.0]
result = mean_absolute_deviation(numbers3)
print(result) 

numbers4 = [10.0, 0.0, 1.0]
result = mean_absolute_deviation(numbers4)
print(result) 

This script defines a function called `mean_absolute_deviation` that takes a list of numbers and returns the Mean Absolute Deviation. The MAD is calculated by finding the mean of the list, then calculating the squared difference between each number and the mean, and taking the average of the squared differences.

The script also includes several test cases to verify the correctness of the function, and the output will be printed to the console.

Note: You can run this script and compare the output with the provided markdown code block.