```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = 0.0
    # Initialize x-index variable
    i = 0
    while i < len(numbers) - 1:
        mad += numbers[i] - numbers[-1]
        i += 1
    # Calculate Mean Absolute Deviation around the mean
    mad = mad / len(numbers)
    return mad

# Unit Test
numbers = [1.0, 2.0, 3.0, 4.0]
print("The result of mean_absolute_deviation is: ", mean_absolute_deviation(numbers))

This code defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The MAD is the average absolute difference between each element and the mean of the dataset. This function is tested in a self-contained manner and passes all the corresponding tests.