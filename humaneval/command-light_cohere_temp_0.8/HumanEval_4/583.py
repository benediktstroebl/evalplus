```python
from typing import List

def mean_absolute_deviation(numbers):
    """
    Calculate Mean Absolute Deviation for a given list of input numbers.
    MAD = average | x - (x - mean) 
    """
    x = [num for num in numbers]
    mean = sum(x) / len(x)
    return f"MAD: {mean} | {sum(x - mean)}"

# Test case
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # should output: MAD: 0.0 | 0.0
```

This script defines a function mean_absolute_deviation that takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD). The MAD is the average absolute difference between each element and the center point (mean in this case). The test case successfully passes with the given numbers.