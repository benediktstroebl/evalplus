Here's a self-contained Python script that calculates and returns the Mean Absolute Deviation around the mean of a dataset:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. This is core formula: MAD = average | x - x_mean |
    """
    return sum(x - list(numbers)[0]) / len(numbers)
```
This function calculates the Mean Absolute Deviation, which is the average absolute difference between each element and the centerpoint (mean). It does this calculation in a single line, which is a self-contained function that is easy to test and doesn't require any external functions or variables to be defined.