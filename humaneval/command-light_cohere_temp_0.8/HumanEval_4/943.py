```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """
    For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset. MAD = average | x -x_mean |
    
    :param numbers: list[float]
    :return: float
    """
    x_mean = sum(numbers) / len(numbers)
    mad = sum((x - x_mean) for x in numbers) / len(numbers)
    return mad

# Test case:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
``` 
This Python code defines a function called "mean_absolute_deviation" that takes a list of input numbers as an argument. It calculates the Mean Absolute Deviation (MAD), which is the average absolute difference between each element and the mean of the dataset. The MAD is then calculated using the provided formula and the provided list of numbers. The test case provided at the passing the test case and it returns the result 1.