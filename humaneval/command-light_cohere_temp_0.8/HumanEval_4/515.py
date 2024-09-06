```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = math.mean(numbers)
    mad = sum((num - mad) for num in numbers) / len(numbers)
    return mad

# Test case:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 1.0)
```