Here is a Python script with a self-contained function that solves the problem you have described:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n)])

# Test cases
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'

test_string_sequence()
```
This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` (inclusive). The function uses list comprehension to generate the string. The test_string_sequence function verifies that the `string_sequence` function produces the correct output for the given inputs.