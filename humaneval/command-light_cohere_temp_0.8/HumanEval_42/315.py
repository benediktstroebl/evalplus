```python
def incr_list(lst):
    n = len(lst)
    lst[::n] = n + 1
    return lst

# Test suite
def test_incr_list():
    tests = [
        ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123])
    ]

    for test, expected in tests:
        actual = incr_list(test)
        assert actual == expected, f"Test '{test}' failed: {actual} != {expected}"

# Example usage
test_incr_list()
```
The function `incr_list` adds one to the length of the list passed as an argument, effectively increasing all its elements by 1. The test suite has a function's output and checks that the function works correctly for the provided test cases.