Here is a Python script with a self-contained function that solves the problem of filtering integers from a list:

```python
def filter_integers(values):
    result = [x for x in values if isinstance(x, int)]
    return result

# Test case 1: Filter integers from a list
test_values = [3.14, 5, 1, 2, 'abc']
result1 = filter_integers(test_values)
assert len(result1) == 4, "Error: Incorrect output"

# Test case 2: Filter integers from a tuple
test_tup = (3, 5, 6, 7)
result2 = filter_integers(test_tup)
assert len(result2) == 3, "Error: Incorrect output"

# Test case 3: Filter integers from a string
test_str = "abc"
result3 = filter_integers(test_str)
assert len(result3) == 0, "Error: Incorrect output"

# Test case 4: Filter integers from an empty list
test_empty = []
result4 = filter_integers(test_empty)
assert len(result4) == 0, "Error: Incorrect output"
```

This script provides a function `filter_integers` that accepts a list of values. It then uses list comprehension to filter out any values that are not integers. The test cases are applied to ensure the function's correctness.