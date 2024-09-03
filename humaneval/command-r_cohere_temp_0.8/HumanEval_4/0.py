```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation for a list of numbers.
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean:
    MAD = average(|x - x_mean|)
    Args:
        numbers (List[float]): A list of numeric values

    Returns:
        float: Mean Absolute Deviation
    """
    if not numbers:
        return 0.0

    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad
```