```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

```
This code defines a `get_positive` function that takes an input list and returns a new list containing only the positive elements from the input. The `test_get_positive` function tests the `get_positive` function with various input lists, and the assertions in the test function verify that the output of the `get_positive` function matches the expected result.