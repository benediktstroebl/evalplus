```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    lst=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    expect=[123]
]

def test():
    assert max_element(test_max_element) == expect

# Run the test suite
test()
```
This code defines a function `max_element` that calculates and returns the maximum element from a given list. Additionally, it includes a set of test cases using the `test` function, which verifies the correctness of the `max_element` function by comparing its output with the expected result. This ensures that the `max_element` function is self-contained and effectively solves the problem of finding the maximum element in a list. The test suite is then run to execute the code and validate the function's correctness.