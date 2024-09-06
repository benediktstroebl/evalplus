Here is a self-contained Python function that calculates the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation for the input list.

    Calculate the mean of the list and store it in x_mean.
    Calculate the absolute differences between each element of the list and the mean, and store them in a new list called diffs.
    Calculate the sum of the differences and store it in sum_of_dev.
    Calculate the mean of the list - sum of the differences.
    MAD = math.sqrt(sum_of_dev / len(numbers))
    return MAD

```
This function takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) of the dataset.

The Mean Absolute Deviation (MAD) is the average absolute difference between each element and the centerpoint (mean in this case). It uses the "typing" module to make the function more readable and efficient.

This function can be used to calculate the MAD of any given list of numbers, and the result will be returned as a single value.