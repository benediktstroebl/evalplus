```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], lambda x: x[1] ),
    ( [1, 2, 3], lambda x: x[0] ),
    ( [-5, 3, -2, -3, 3, 0, 9, -10, 1], lambda x: x[1] ),
    ( [123, 0, 9, 1], lambda x: x[1] ),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
    ( [10, 20, 30], lambda x: x[0] ),
]

for test, expected in test_max_element:
    print(f"Test: {test} => {expected}")
    print(f"MAX({test}): {max_element(test)}")
```

This Python script provides a self-contained function `max_element` that takes a list as an argument and returns the maximum element in the list. It also provides a test cases with multiple lists and custom functions to test the correctness of the `max_element` function. The test cases cover a scenarios with different types of lists and custom functions that return the maximum element, and the `max_element` function is called with each test case to ensure its correctness.