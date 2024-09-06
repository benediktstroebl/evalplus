Here is a self-contained Python function that calculates and returns the mean absolute deviation:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    return the MAD calculation:
    sums up all absolute values of the differences of each element in the list and the total is divided by the total number of elements in the list
    """
    return sum(map(lambda x: abs(x - numbers.mean()), numbers)) / len(numbers)
```

This code defines a function mean_absolute_deviation that takes a list of numbers as input and returns the mean absolute deviation of the list.