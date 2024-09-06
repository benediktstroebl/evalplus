Here is a self-contained Python function that solves the given problem:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]):
    # Calculate mean of the input numbers
    mean = sum(numbers)/len(numbers)
    # Calculate MAD, the average absolute difference between each element and the mean
    MAD = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return MAD
# Test the function with a sample of numbers
numbers = [1.0, 2.0, 3.0, 4.0]
print("Mean Absolute Deviation is: %.2f" % mean_absolute_deviation(numbers))
```
The function MeanAbsoluteDeviation takes a list of numbers as input and returns the Mean Absolute Deviation (MAD). This is the average absolute difference between each element and the mean of the dataset. The function uses the mathematical formula MAD = average | x - x_mean |, which computes the sum of squared differences between each element and the mean.