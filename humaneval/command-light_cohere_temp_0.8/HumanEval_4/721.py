```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset."""
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Example of test of function:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.9) == True)

# Another example test:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 1.0) == True)

This code defines a Python function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) for a list of numbers. The function then returns the MAD value, which is then tested against the expected result (0.9) and (1.0).00.