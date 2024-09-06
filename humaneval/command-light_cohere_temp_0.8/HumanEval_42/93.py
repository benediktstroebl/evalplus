```python
def incr_list(lst):
    new_elements = []
    for num in lst:
        new_elements.append(num + 1)
    return new_elements

# Unit tests
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert list(incr_list(test_list)) == expected

# Test suite
test_incr_list()
```

This code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The function iterates through the test_incr_list function to test the correctness of the `incr_list` function. The test suite contains a test case, which passes the test and demonstrates the functionality of the `incr_list` function.