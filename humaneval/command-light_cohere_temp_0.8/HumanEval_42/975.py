```python
def incr_list(lst):
    return [lst[-1]+1 for lst in lst]

# Test function for incr_list
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(lst) == [6, 3, 6, 4, 6, 4, 10, 1, 124]
```

This function `incr_list` takes a list as an argument and returns a new list with the last element of the original list incremented by 1. The test function `test_incr_list` tests if the `incr_list` function correctly works by creating a list of numbers and passing it into the function, and then checking if the returned list matches the expected output.