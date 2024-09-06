```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation
    MAD = sum([x - mean for x, mean in zip(numbers, numbers[::mean]))) / len(numbers)
    return MAD

# Unit test for function
def test_mean_absolute_deviation(numbers):
    assert mean_absolute_deviation(numbers) == 0.0

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(test_mean_absolute_deviation(numbers) == 0.0)
```
This script defines a function **`mean_absolute_deviation`** that computes the Mean Absolute Deviation for a given list of numbers. It then has a unit test **`test_mean_absolute_deviation`** to check its correctness, and an example **`numbers`** that is passed to this function to test its output.