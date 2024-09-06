Here's a Python script with a self-contained function that solves the problem you've described, along with a series of tests to validate its correctness:
```python
# Ensure the robustness of the calculation with proper typing
from typing import List, Dict, Union

# Function to calculate the mean absolute deviation
def mean_absolute_deviation(numbers: List[Union[int, float]]) -> float:
    return mad(numbers, mean(numbers)) 

# Util function to calculate mean, handling empty lists
def mean(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)

# Util function to calculate mean absolute deviation
def mad(numbers: List[Union[int, float]], center: float) -> float:
    deviations = [abs(x - center) for x in numbers]
    return sum(deviations) / len(numbers)

# Unit tests
def test_mad_with_valid_input():
    # Test case from the problem statement
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    # Additional test cases with positive integers
    assert mean_absolute_deviation([0, 1, 2, 3, 4, 5]) == 1.0
    assert mean_absolute_deviation([10, 11, 12, 13, 14]) == 1.0
    # Additional test cases with negative integers
    assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 2.0
    assert mean_absolute_deviation([-10, -11, -12, -13, -14]) == 1.0
    # Additional test cases with floats
    assert mean_absolute_deviation([0.1, 0.2, 0.3, 0.4, 0.5]) == 0.3
    assert mean_absolute_deviation([-0.1, -0.2, -0.3, -0.4, -0.5]) == 0.6
    # Test case with just one element
    assert mean_absolute_deviation([10]) == 0.0

def test_mean_with_empty_list():
    # Test case where input list is empty
    assert mean([]) == None  # Type hint as None for mypy compatibility (see comment above)

def test_mad_with_empty_list():
    # Test case where input list is empty
    assert mad([], 0) == None  # Type hint as None for mypy compatibility (see comment above)

def test_mad_with_non_list_input():
    # Ensure function raises TypeError for non-list input
    assert isinstance(mean_absolute_deviation("hello"), TypeError)
    assert isinstance(mean_absolute_deviation(10), TypeError)

# Run the tests if the script is executed directly
if __name__ == "__main__":
    import unittest
    unittest.main()
```
This script includes:
- The `mean_absolute_deviation()` function, which takes a list of numbers and returns the mean absolute deviation for those numbers.
- The `mean()` function, which calculates the mean of a list of numbers and raises an error if the list is empty.
- The `mad()` function, which calculates the mean absolute deviation of a list of numbers about a given center.
- A series of unit tests (`test_mad_with_valid_input`, `test_mean_