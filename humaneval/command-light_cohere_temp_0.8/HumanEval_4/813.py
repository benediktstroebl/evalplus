Here's the solution to the problem:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Test Case 1
print("Test Case 1: Result: ", mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))

# Test Case 2
print("Test Case 2: Result: ", mean_absolute_deviation([10.0, 20..0, 30.0, 40.0]))
# Test Case 3
print("Test Case 3: Result: ", mean_absolute_deviation([1.0, 10.0, 2.0, 20.0]))
```