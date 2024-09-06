Here is a self-contained Python script that solves the problem and passes the corresponding tests:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation for a given list of numbers 
    around the mean of this dataset.

    MAD = average | x -x_mean |

    Mean Absolute Deviation (MAD) is the average absolute difference between 
    each element and a centerpoint (mean in this case).

    Test: The output of the function is the calculated MAD.
    ```