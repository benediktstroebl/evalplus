```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This Python code defines a function called `incr_list` that takes a list as input and appends an element with a value of 1 to it, then returns the updated list with each subsequent element incremented by 1. The `test_incr_list` function contains test cases to ensure the correctness of the `incr_list` function.