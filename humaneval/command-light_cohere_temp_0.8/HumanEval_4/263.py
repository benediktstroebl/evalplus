Here is a Python script that calculates the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Declare variables and the mean of the dataset
    mean = sum(numbers) / len(numbers)
    # Calculate the Absolute Deviation around the mean
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad
# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = 0.1644000  #