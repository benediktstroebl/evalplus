Here's the solution:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = sum(x - x_mean for x, x_mean in zip(numbers, [float(num) for num in numbers]))) / len(numbers)
    return MAD

#Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)

```
Do you need help with anything else?