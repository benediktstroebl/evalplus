Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test case to demonstrate its usage:
```python
# Ensure testing is initiated only when the MAD function is defined
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        return 0.0  # Handle empty list to avoid division by zero
    
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad

# Test case for the mean_absolute_deviation function
def test_mad_calculation():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([2, 3, 4, 5, 6, 7]) == 0.575

# Run the test case when the script is directly executed
test_mad_calculation()
```

This script defines the `mean_absolute_deviation` function to calculate the Mean Absolute Deviation of a list of numbers. It then provides a test case (`test_mad_calculation`) that calls this function with two different lists of numbers and asserts that the returned Mean Absolute Deviation is correct.

When the script is directly executed, it runs the test case to demonstrate the usage of the `mean_absolute_deviation` function and verifies its correctness against the expected results.