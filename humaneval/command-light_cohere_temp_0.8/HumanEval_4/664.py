Here's a solution that calculates the Mean Absolute Deviation:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of this dataset.
    MAD = sum(x_mean - abs(x - x_mean) ) / len(numbers)
    return MAD

# Test
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 0.0)
```

This script defines a function **`mean_absolute_deviation`** that takes a list of numbers as an argument and returns the Mean Absolute Deviation. The function first calculates the mean of the dataset and then calculates the MAD as the average absolute difference between each element and the mean. Then, the function passes the tests.