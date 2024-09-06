Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test case to validate its correctness:
```python
# Importing the necessary type hinting module
from typing import List

# The function to be tested
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        return 0.0  # Handle empty list case
    
    # Calculate mean of the list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Return the mean of absolute deviations
    return sum(absolute_deviations) / len(numbers)

# Test case for the function
def test_mad():
    """ Test case for the mean_absolute_deviation function """
    
    # Test empty list case
    assert mean_absolute_deviation([]) == 0.0
    
    # Test list with one element
    assert mean_absolute_deviation([1.0]) == 0.0
    
    # Test list with multiple elements
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    
    # Test list with negative numbers
    assert mean_absolute_deviation([1.0, -2.0, 3.0, -4.0]) == 2.0
    
    # Test list with a large number of elements
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    assert mean_absolute_deviation(numbers) == 3.0

# Run the test case
test_mad()
```

In this script, the `mean_absolute_deviation` function calculates the mean of the input list of numbers and then calculates the absolute deviation of each number from the mean. It then returns the average of these absolute deviations, which is the Mean Absolute Deviation.

The `test_mad` function provides test cases to validate the behavior of the `mean_absolute_deviation` function for various scenarios, including an empty list, lists with one element, lists with multiple elements, and lists with negative numbers.