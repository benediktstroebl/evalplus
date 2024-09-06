```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers in the list
    mean = sum(numbers) / len(numbers)
    # Calculate the average absolute deviation of the numbers from the mean
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    + numbers of floats.
    assert mean_mean_absolute_deviation(numbers) == 0.72
   

print("Test passed")
```