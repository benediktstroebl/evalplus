```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test1()
    test2()
```
This code defines a function `incr_list` that returns a list with elements incremented by 1. Two test cases are test functions are provided to validate the `incr_list` function. The test cases pass theate successfully, and demonstrate the correct functionality of the `incr_list` function.