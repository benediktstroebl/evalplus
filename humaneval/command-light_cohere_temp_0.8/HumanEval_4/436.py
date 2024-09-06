```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Mean Absolute Deviation is a measure of the average absolute difference between each
    element and the mean of this dataset. This is a the average of those absolute
    differences and returns the result.

    :paramers
    numbers: The list of numbers to calculate the MAD for
    :return: The Mean Absolute Deviation of the given numbers
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(num - mean) for num in numbers) / len(numbers)
    return mad
```