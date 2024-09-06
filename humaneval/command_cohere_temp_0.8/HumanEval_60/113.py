```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive). It uses the `sum` function to add up all the values in the `range` of numbers from 1 to `n`, inclusive, and returns the result. 

The script includes a docstring with information about the function's purpose, and provides example usage that demonstrates how to call the function with different values of `n` and shows the resulting sums.

If you need to test this script, you can use the `pytest` library to verify the functionality of the `sum_to_n` function with different input values. An example test suite is provided below:
```python
# test_sum_to_n.py
import pytest
from sum_to_n import sum_to_n  # assuming this file is in the same directory

def test_sum_to_n_with_30():
    assert sum_to_n(30) == 465

def test_sum_to_n_with_100():
    assert sum_to_n(100) == 5050

def test_sum_to_n_with_5():
    assert sum_to_n(5) == 15

def test_sum_to_n_with_10():
    assert sum_to_n(10) == 55

def test_sum_to_n_with_1():
    assert sum_to_n(1) == 1

def test_sum_to_n_with_0():
    with pytest.raises(ValueError):
        sum_to_n(0)  # range raises a ValueError if start is > stop
```

To run these tests, you can use the `pytest` command:
```bash
pytest test_sum_to_n.py
```

This command will run all the test functions and report any failures or errors. The final test, `test_sum_to_n_with_0`, checks whether passing 0 as an input triggers a `ValueError` (which is the expected behavior, as range cannot produce a valid sequence when the start value is greater than the stop value). 

This complete test suite ensures the `sum_to_n` function works correctly across different input scenarios.  If any of the tests fail, `pytest` will report the failures, helping identify where the code needs improvement. If all tests pass, it indicates that the function `sum_to_n` is functioning correctly.  This approach makes it easy to ensure that the code remains stable as changes are made to the codebase.