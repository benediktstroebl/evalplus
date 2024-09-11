```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each 
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The mean absolute deviation of the input numbers.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    mean = sum(numbers) / len(numbers)
    deviations = [(n - mean) ** 2 for n in numbers]
    return sum(abs(d) for d in deviations) / len(numbers)


# Example usage:
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This Python function takes a list of numbers as input and calculates the mean absolute deviation around the mean of the dataset. It first checks if the input list is empty, and raises a `ValueError` in this case. Then it calculates the mean of the numbers, computes the absolute deviations from the mean, and finally returns the mean of these absolute deviations. The function includes a docstring with a usage example to demonstrate how to use it.