Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test suite to verify its correctness:
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
    # Ensure the input list is not empty and all elements are floats
    if not numbers or not all(isinstance(n, float) for n in numbers):
        raise ValueError("Input list must be a non-empty list of floats")
        
    # Calculate mean and deviation
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(absolute_deviations) / len(numbers)


# Separate test suite
def test_mad():
    # Test with a simple list of numbers
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.0

    # Test with an empty list
    with pytest.raises(ValueError):
        mean_absolute_deviation([])

    # Test with a list containing non-numeric elements
    with pytest.raises(ValueError):
        mean_absolute_deviation([1, 2, '3', 4, 5])

```

In this script, the `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers as described in the problem statement. The `test_mad` function provides a test suite with multiple test cases to validate the correctness of the `mean_absolute_deviation` function. 

To run these tests, you would need to have `pytest` installed. If you don't have it, you can install it using `pip`: 
```bash
pip install pytest
``` 

Then, you can use the following command to run the tests:
```bash
pytest -v
``` 

The command above will execute the test suite and show you a detailed report on the status of each test case, including those we defined above. 

This separation of concerns into a well-tested function and a robust test suite is a hallmark of good software engineering practices.