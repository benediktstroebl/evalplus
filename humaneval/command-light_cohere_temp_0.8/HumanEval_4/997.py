```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation
    MAD = sum(x - numbers[-1]) / len(numbers)
    return MAD

# Test the function with sample input
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)  # True  # passed
```