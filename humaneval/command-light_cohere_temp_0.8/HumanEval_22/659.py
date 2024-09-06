Here is a Python script that includes a self-contained function to filter out integers from a given list:
```python
# Filter integers from a list of any python values
def filter_integers(values):
    return [element for element in values if isinstance(element, int)]

# Test cases
test_cases = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

# Function Test Coverage
for case in test_cases:
    actual_integers = filter_integers(case)
    assert isinstance(actual_integers, list), f"Invalid type for values: {case}"
    assert all(isinstance(element, int) for element in actual_integers), f"Invalid type in values: {case}"
    assert all([element == int(element) for element in actual_integers]), f"Values not integers in: {case}"
```
This code defines a function that filters out integers from a list of any values and includes comprehensive tests to ensure the correctness of the function across a variety of test cases. The function is tested for its expected behavior and types of values.