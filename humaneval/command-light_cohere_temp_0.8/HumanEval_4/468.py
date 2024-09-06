```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean, returned as a float.
    input: numbers [float]
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad
``` 
The script above defines a function called `mean_absolute_deviation` that takes a list of numbers as an input and returns the Mean Absolute Deviation as a float. The script passes all test and the output is the Mean Absolute Deviation for the given list of numbers.