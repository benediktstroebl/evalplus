```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # mean calculation function
    mean = sum(numbers) / len(numbers)
    # return the average absolute deviation of the dataset
    return abs(mean - numbers[len(numbers) / 2])
```
This function takes a list of numbers and returns the Mean Absolute Deviation of this dataset.