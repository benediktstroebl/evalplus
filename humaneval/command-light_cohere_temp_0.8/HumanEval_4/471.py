```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    # Calculate mean of the dataset
    mean = sum(numbers) / len(numbers)
    # Calculate Mean Absolute Deviation
    MAD = mean | numbers[-1] - mean
    return MAD
``` 

The function uses the Python 'sum' function to add up all the numbers in the list, and the 'len' function to get the length of the list. The function then divides the result by the number of elements in the list and then stores the result in the variable 'MAD'.