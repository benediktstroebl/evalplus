```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD is the average absolute difference between each
    element and a centerpoint (mean in this case).
    MAD = average | x - x_mean |
    return MAD
```

This function takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of the dataset.

The Mean Absolute Deviation (MAD) is the average absolute difference between each element and the mean of the dataset.

This function could be tested by passing in a sample list of numbers and verifying that the returned value is a correct calculation of the Mean Absolute Deviation.