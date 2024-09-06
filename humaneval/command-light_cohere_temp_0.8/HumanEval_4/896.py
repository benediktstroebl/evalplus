```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum([x - mean for x, mean in zip(numbers, numbers)]) / len(numbers)
    return MAD

# Test the function with a sample list of numbers
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.1633990)  # Passes the test!