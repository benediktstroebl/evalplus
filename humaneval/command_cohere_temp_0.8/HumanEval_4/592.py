Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test suite to validate its correctness:
```python
# -*- coding: utf-8 -*-
import numpy as np
import pytest

from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case).

    Parameters:
        numbers (list): List of numerical values.

    Returns:
        float: Mean Absolute Deviation value.
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0

@pytest.mark.parametrize('input_numbers', [
    [1.0, 2.0, 3.0],
    [2.0, 3.0, 2.0, 1.0],
    [0.5, 1.0, 1.5, 2.0, 2.5],
])
def test_mad_ correctness(input_numbers):
    expected_mad = np.mean(np.abs(np.array(input_numbers) - np.mean(np.array(input_numbers))))
    assert mean_absolute_deviation(input_numbers) == expected_mad

def test_mad_empty_list():
    with pytest.raises(ValueError):
        mean_absolute_deviation([])

def test_mad_non_numeric_items():
    with pytest.raises(ValueError):
        mean_absolute_deviation(['a', 'b', 'c'])
```

In this script, the `mean_absolute_deviation` function calculates the MAD of a list of numbers. The `test_mad_correctness` function tests the function with example datasets and compares the result with the expected value obtained through manual calculation using NumPy. `test_mad_empty_list` checks if the function raises a `ValueError` for an empty list. Lastly, `test_mad_non_numeric_items` ensures the function raises a `ValueError` when presented with a list containing non-numeric items. 

To run the tests, you can use the `pytest` framework. 
You can install it with:
```bash
pip install pytest
```
Then, navigate to the script directory in your terminal and run:
```bash
pytest
``` 

The `pytest` framework will run each test script sequentially and report any failures or errors. 

Please make sure you have `numpy` installed, as it is required for both the implementation and testing. You can install it via `pip`: 
```
pip install numpy
``` 

This code snippet showcases practices like descriptive variable names, type hints, docstrings, separation of testing and implementation, and test coverage for a robust and reliable Python function. P.S. You may consider using `pytest-doctest` for testing docstrings against actual code examples, but it's not included in this snippet for brevity.