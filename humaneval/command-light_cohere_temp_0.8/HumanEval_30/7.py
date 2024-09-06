```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```
This Python code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. The function uses a `itertools.range list comprehension with a boolean condition: `num >= 0`. The test suite `test_get_positive` contains two test cases that verify the correctness of the `get_positive` function by comparing the returned lists with the expected results. 

The test suite uses the `assert` statement to check if the test cases pass or not.