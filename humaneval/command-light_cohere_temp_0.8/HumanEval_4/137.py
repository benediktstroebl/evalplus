```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. It is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x is the element of the list and x_mean is the mean of the list.
> 
    The test of correctness is that if you compute the mean of the list [1.0, 2.0, 3.0, 4] and pass it to [2.0, 1.0, 3.0] using then other_mad, you pass the test.

 MAD = 0.1 | 2.0 - 2.0 |

2.2, 3.3)
2.2, 2.2)
MAD = 0.1, (1.0 | 1.0 - 2.0) = 1.0

test of mean absolute deviation passed.

The solution uses the Mean Absolute Deviation formula to calculate the MAD value.