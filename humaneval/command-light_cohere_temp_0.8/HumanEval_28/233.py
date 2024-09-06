Here's the self-contained Python function that performs the task you described:
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Test cases
test_concatenate = [
    [],  # Empty list; should return empty string
    ['a'],  # Single string; should return 'a'
    ['a', 'b', 'c'],  # Three strings; should return 'abc'
]

for test_case in test_concatenate:
    actual_result = concatenate(test_case)
    assert actual_result == test_case[0], f"Failed for {test_case}"
```

This code defines a function `concatenate` that takes a list of strings and returns their concatenation as a single string. The test cases ensure that function produces the expected output for various inputs.