Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the input list
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad
```
This script includes the function `mean_absolute_deviation()` that takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD) of the list, returning the result as a float. It sums the absolute values of the deviations from the mean for each number in the list, then divides by the number of elements to get the average deviation. Test cases can be added to verify the functionality of the script. 
```python
# Test Cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(f">>>mean_absolute_deviation({numbers})\n{mean_absolute_deviation(numbers)}")
``` 
This will output:
```
>>>mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
``` 
The test case verifies the MAD calculation for the input list [1, 2, 3, 4].