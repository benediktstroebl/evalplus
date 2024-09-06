Here's a Python script with a self-contained function that solves the problem you've outlined, along with a sample test to verify its correctness:
```python
# Importing the necessary type annotation module
from typing import List

# The function to calculate the mean absolute deviation of a list of numbers
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Return the mean of the absolute deviations
    return sum(absolute_deviations) / len(numbers)

# Sample test case with corresponding assertion
def test_mad_function():
    # Test case for a list with an even number of elements
    numbers = [1.0, 2.0, 3.0, 4.0]
    assert mean_absolute_deviation(numbers) == 1.0

# To run the test, use this command in your CLI:
# pytest -v
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers. It is accompanied by a test case, `test_mad_function`, which verifies the correctness of the function's implementation using the `pytest` framework.

You can run this code to see the test outcome, or use this command to run the test exclusively:
```python 
pytest -v
``` 
This will run the test and provide you with the results. 

Let me know if you encounter any issues or if you'd like to further discuss test cases or any other topics!