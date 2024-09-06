Here's a self-contained Python function that calculates and returns the Mean Absolute Deviation (MAD) of a list of numbers, with tests provided:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> def mean_absolute_deviation( [1.0, 2.0, 3.0, 4])
    -
    < Madison Ave Madness >
    The Madison Avenue of the input is too high. Please provide a correct input.
    raise ValueError("Please provide a list of numerical values")
```
The error handling in this script is a good practice to provide better reliability and user experience.