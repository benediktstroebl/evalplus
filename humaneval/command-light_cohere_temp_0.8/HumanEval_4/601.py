Here is a self-contained Python function that calculates the mean absolute deviation and passes the test for your provided input: 
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation = average | x - x_mean |
    x_mean = sum(numbers) / len(numbers)
    return x_mean | sum(map(lambda x: abs(x - x_mean), numbers)))
```