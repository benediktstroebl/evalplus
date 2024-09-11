### Mean Absolute Deviation Calculator

Here's a Python script that calculates the Mean Absolute Deviation (MAD) for a given list of numbers:

```markdown
### Python Code

```python
from typing import List

def calculate_mean(numbers: List[float]) -> float:
    """ Calculate the mean of a list of numbers """
    return sum(numbers) / len(numbers)


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = calculate_mean(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

### How it works:

1. The `calculate_mean` function calculates the mean of a list of numbers.
2. The `mean_absolute_deviation` function takes a list of numbers, calculates the mean using `calculate_mean`, and then calculates the absolute deviation of each number from the mean. It then returns the average of these absolute deviations.
3. In the example usage, we create a list of numbers, calculate the Mean Absolute Deviation, and print the result.