```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """

    # Declaring list to store the mean of input dataset
    mean = 0.0

    for num in numbers:
        mean += num

    # Calculate the mean of input dataset
    mean /= len(numbers)

    # Calculate the absolute difference between each element and the mean
    mad = 0.0
    for num in numbers:
        mad += (num - mean) ** 2

    # Return the Mean Absolute Deviation
    return mad
``` 
The function takes a list of numbers and calculates the Mean Absolute Deviation around the mean of the dataset.