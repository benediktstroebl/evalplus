```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates the Mean Absolute Deviation for a list of numbers, 
    around the mean of the dataset.
    """
    MAD = sum((x - (x - mean) ** 2) ) / len(numbers)
    return MAD

# Basic test cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
numbers = [1.0,2.0,3.0,4]print(mean_absolute_deviation(numbers)) == 0.0)
numbers = [0.0, 0.0, 0.0, 3.0]
print(mean_absolute_deviation(numbers)) == 0.0)
print(mean_absolute_deviation([4.0, 3.0, 2.0])
print(mean_absolute_deviation([4.0]*100))
```