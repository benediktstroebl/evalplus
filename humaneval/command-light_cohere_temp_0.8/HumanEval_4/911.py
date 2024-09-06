Here's the self-contained Python function:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD = average | x - - x_mean |
    """

    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)

    # Calculate the average absolute deviation of the dataset
    MAD = sum((x - mean) ** 2 for x in numbers) / len(numbers)

    return MAD
```
This function takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) value for the dataset.  The purpose of this MAD is to calculate the average absolute difference between each element and a centerpoint (mean in this case). 

It uses the Pythagorean square of a difference between an element and the mean to calculate the average absolute deviation.