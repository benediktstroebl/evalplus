```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
   
    individual numbers.
    mean = sum(numbers)/len(numbers)
    # Remove mean from numbers list
    numbers.remove(mean)
    # Sort list of numbers in ascending order
    numbers.sort()
    array of numbers is sorted in ascending order.
    # Calculate Sum of squared differences from mean
    sum_of_squared = sum(f ** 2 for f in numbers)
    # Calculate Mean of squared differences from mean
    mean_of_squared = sum_of_squared / len(numbers)
    # Calculate Mean Absolute Deviation
    mad = mean_of_squared | mean
    return mad
```