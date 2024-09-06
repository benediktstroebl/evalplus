```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset."""
    return sum((x-mean) ** 2 for x, mean in zip(numbers, numbers.mean())) / len(numbers)
```
Do you need any help with anything else?