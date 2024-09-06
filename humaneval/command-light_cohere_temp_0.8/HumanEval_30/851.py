```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test suite
test_suite = []

# Unit test 1
def test_get_positive():
    test_suite.append(get_positive([-1, 2, -4, 5, 6]))
    test_suite.append(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

# Run the test suite
test_suite
```

This script defines a function `get_positive` that takes a list as an argument and returns a new list with only the positive elements from the input list. It then includes a test suite with a few test cases to ensure the correctness of the function. You can expand the the run the test suite using the `test_suite` variable and the `test_get_positive` function.