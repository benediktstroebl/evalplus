Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and a sample test:
```python
# md5ebec4c54e8c5d5e638294807d4a0f33
# Functions to calculate Mean Absolute Deviation
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    mean = sum(numbers) / len(numbers)
    dev = []
    for n in numbers:
        dev.append(abs(n - mean))
    return sum(dev) / len(numbers)

# Example usage and test:
numbers = [1, 2, 3, 4, 5]
print(mean_absolute_deviation(numbers))  # Should print: 1.0
```