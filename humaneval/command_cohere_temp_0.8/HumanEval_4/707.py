Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test case to demonstrate its usage:
```python
# Importing the necessary typing module
from typing import List

# The function to calculate the mean absolute deviation
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Ensure the input list is not empty and all values are numeric (float)
    if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input list must be a non-empty list of numbers")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Return the mean of the absolute deviations
    return sum(absolute_deviations) / len(numbers)

# Sample test case
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(f">Mean Absolute Deviation: {mean_absolute_deviation(numbers)}")
```

You can run this code to see the result of the calculation, and the script includes a usage example for the `mean_absolute_deviation` function. Feel free to adapt this code to your needs or scale it up for more extensive testing or real-world usage.