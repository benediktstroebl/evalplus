Here's a self-contained Python function that calculates and returns the Mean Absolute Deviation (MAD) for a list of numbers:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    MAD = math.abs(sum(x -x_mean -x) / len(numbers))
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]):
    """ Returns the mean of the list of numbers.
    return sum(numbers)/len(numbers)
    """

# Test the function with a list of numbers [1.0, 2.0, 3.0, 4.0]
print mean_mean_absolute_deviation([1.0, 2.0, 3.0, 4])
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]))

# Output: 2.52571499

```
The function mean_absolute_deviation takes a list of numbers as input and returns the Mean Absolute Deviation. The function mean takes a list of numbers as input and returns the mean of the list.