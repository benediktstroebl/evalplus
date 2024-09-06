Here is a Python script that solves the problem of finding the mean absolute deviation (MAD) of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the average absolute deviation around the mean
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return mad

# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8, 8, 9]
test_mean_absolute_deviation(numbers)
assert math.isclose(mean_absolute_deviation(numbers), 1.142857)

# Test with empty list
numbers = []
test_mean_absolute_deviation(numbers)
assert math.isclose(mean_absolute_deviation(numbers), 0.0)

# Test with one element list
numbers = [9.0]
test_mean_absolute_deviation(numbers)
assert math.isclose(mean_absolute_deviation(numbers), 9.0)

```
The function Mean Absolute Deviation calculates the mean and then computes the MAD of the list, testing it with a variety of test cases.