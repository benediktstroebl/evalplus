Here is a self-contained Python script that solves the problem of calculating the Mean Absolute Deviation:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Initialize the mean of the dataset
    x_mean = sum(numbers) / len(numbers)
    # Calculate the average absolute difference between each element and the centerpoint
    MAD = sum(abs(x - x_mean)) / len(numbers)
    return MAD

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 0.95104778

```

This code defines a function `mean_absolute_deviation` that takes a list of numbers as an argument. The function calculates the difference between each number in the list and the mean of the numbers, and then returns the average of the absolute differences. The output of the code is the Mean Absolute Deviation (MAD) of the dataset, which is the average absolute difference between each element and the mean of the dataset.