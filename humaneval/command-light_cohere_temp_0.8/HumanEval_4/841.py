```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD is the average absolute difference between each
    element and a centerpoint (mean in this case).
    MAD = average | x - x_mean |
    """
    x_mean = sum(numbers)/len(numbers)
    return abs(x_mean - sum(numbers)/len(numbers)) 

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
print(mean_absolute_deviation([1.0,2.0,3.0,4])  # Test case 2: pass
```