Here's a Python script with a self-contained function that solves the problem you've outlined, along with a sample test to verify its correctness:
```python
# Importing the necessary type hinting module
from typing import List

# Defining the MeanAbsoluteDeviation function
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Ensure the input list is not empty and all elements are floats
    if not numbers or not all(isinstance(n, float) for n in numbers):
        raise ValueError("Input list must be a non-empty list of floats")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Return the mean of the absolute deviations
    return sum(absolute_deviations) / len(numbers)

# Sample test case
def test_mad():
    """ Test the correctness of the MeanAbsoluteDeviation function
    Case: Input list with single number (should result in MAD of 0)
    """
    assert mean_absolute_deviation([1.0]) == 0.0

# Running the test case when this script is directly executed
test_mad()
```

In this script, the `mean_absolute_deviation` function calculates the MAD as described, and the `test_mad` function provides a simple test case to validate the functionality. You can add more comprehensive tests as needed.