Here's the self-contained Python function to calculate the Mean Absolute Deviation (MAD) of a list of numbers:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    # store the mean of the list
    x_mean = sum(numbers) / len(numbers)
    # store the list of absolute deviations from x_mean
    mad = [abs(num - x_mean) for num in numbers]
    # sort the list of absolute deviations in ascending order
    mad = sorted(mad)
    # return the mean of the list of absolute deviations
    return math.mean(mad)
```
This function, mean_absolute_deviation, takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of this dataset. It achieves this calculation by computing the absolute deviation of each element in the list from the centerpoint (mean), and then returns the mean of the absolute deviations. 

Note that this implementation uses Python's typing module and the math library to make the function more readable and efficient.