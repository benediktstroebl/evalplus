```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Initialize variables
    mean = sum(numbers) / len(numbers)
    x = 0
    for number in numbers:
        x += abs(number - mean)
    MAD = x / len(numbers)
    return MAD
# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Expected output: 1.0
```
This script defines a function called **mean_absolute_deviation** that calculates the Mean Absolute Deviation (MAD) for a list of numbers. The function uses the type hint **List[float]** to indicate that the function expects a list of numeric values as input. It calculates the MAD by calculating the average of the absolute differences between each element and the mean of the dataset. The function then returns the MAD value.