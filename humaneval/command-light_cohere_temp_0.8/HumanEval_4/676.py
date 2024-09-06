```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset.

    Mean Absolute Deviation. The average absolute difference between each element and the mean. 
    The MAD is the average | x - x_mean | where x is each element of the list and x_mean is the mean of the list.
    """ return float
```

def test_mean_absolute_deviation(numbers):
    # Test the function
    mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 0.2
   0
1.1

print(f'Test passed!