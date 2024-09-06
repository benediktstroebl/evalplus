Here's the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset
    
    Returns: Mean Absolute Deviation.
    """
    -> from numbers: List[float]
    numbers.mean = sum(numbers)/len(numbers)
    mad = sum((x - mean) for x in numbers) / len(numbers)
    return mad
```
The function take a list of floating-point input numbers and calculates the Mean Absolute Deviation around the mean of the dataset.

The Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case).