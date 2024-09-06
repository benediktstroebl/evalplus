Here's a self-contained Python function that filters integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []]
]

for test_case in test_cases:
    actual_result = filter_integers(test_case)
    expected_result = [5]  # int(3.14) is an int, so we expect [5]

    print(f"Test case {test_case}:\n {actual_result}\nvs. { {expected_result}\n")
    assert actual_result == expected_result
```

This script defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input. The test cases are defined to validate the behavior of the function for different input scenarios.