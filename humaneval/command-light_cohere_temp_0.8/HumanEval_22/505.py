```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_cases = [
    [],  # Empty list
    ['a', 3, 'four', 5],  # Non-integer values
    [1, 2, 3],        # Integers only
    [1, 2, 3, 'abc'],   # Mixed values with integers and non-integer
]

for values in values_test_cases:
    actual_result = filter_integers(values)
    expected_result = [x for x in values if isinstance(x, int)]
    assert actual_result == expected_result, f"Error in filtering {values}"
```

This script defines a function `filter_integers` that filters a given list of values and returns a new list containing only the integers. It then provides a test cases to the function, and uses the `assert` assertion to check if the actual result matches the expected result. 

You can use this function to filter integers from a list of any python values.