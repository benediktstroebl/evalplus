Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and a testing area:
```python
# MAD Calculation
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if len(numbers) < 1:
        return "Please provide a list of numbers to calculate MAD."
    mean = sum(numbers) / len(numbers)
    mad = sum( abs(x - mean) for x in numbers) / len(numbers)
    return mad

# Test Cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(f">Mean of provided dataset: {mean_absolute_deviation(numbers)}")
```

This script includes a function called `mean_absolute_deviation()` that calculates the mean absolute deviation of a list of numbers. It initially checks if the input list is empty, returning a message if it is. It calculates the mean and sum of absolute deviations for the list of numbers provided otherwise. Finally, it returns the mean absolute deviation (MAD). 

The code includes a test case to illustrate its usage and should be modified to fit your specific tests. Adjust the test case list (`numbers`) according to your needs.