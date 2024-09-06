Here's a self-contained Python function that calculates the Mean Absolute Deviation:
```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) ->
    # Define the mean of the list
    mean = sum(numbers) / len(numbers)
    # Calculate the absolute deviation of each element in the list
    deviations = [(x - mean) ** 2 for x in numbers]
    # Calculate the sum of deviations
    total_deviation = sum(deviations)
    # Return the Mean Absolute Deviation
    return total_deviation / len(numbers) if len(numbers) != 0 else float("INFINITE")
```
The `mean_absolute_deviation` function takes a list of numbers as input and returns the Mean Absolute Deviation of the dataset, which is a measure of the average absolute difference between each element and the mean of the data.