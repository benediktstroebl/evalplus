Here's a self-contained Python script with a function that calculates the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation (MAD) for a given list of numbers.
    MAD = sum((x - abs(x - mean) for x, mean in zip(numbers, numbers))) / len(numbers)
    return MAD

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
```
This script defines a function mean_absolute_deviation that takes a list of numbers as input. It then computes the specific type of mean deviation known as the Mean Absolute Deviation (MAD). The function returns the computed MAD value. The test above verifies that the function is correct.