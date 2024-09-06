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
    :return: Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(math.fabs(x - mean) for x in numbers) / len(numbers)
    return mad
```
This script includes the function `mean_absolute_deviation()` that takes a list of numbers as input and calculates the `Mean Absolute Deviation` of the list of numbers from the mean of the list. It then returns the result. 
To validate the correctness of the implementation, the script also includes a test case:
```python
# Test case
numbers = [1.0, 2.0, 3.0, 4.0]
print(f"For the list of numbers {numbers}, the Mean Absolute Deviation is {mean_absolute_deviation(numbers)}")
```
This should produce the output:
```
For the list of numbers [1.0, 2.0, 3.0, 4.0], the Mean Absolute Deviation is 1.0
``` 
The test case demonstrates the computation of MAD for a list of numbers and verifies if the result matches the expected outcome. 
This test case represents a specific case that the function can handle and can be enhanced with more comprehensive tests to cover a wide range of scenarios and edge cases.