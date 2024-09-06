```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}" * (n + 1)

# Test case 1: Validate the function with different input values
def test_string_sequence(testCase: int) -> None:
    assert string_sequence(testCase) == f"0 {testCase}".format_string(testCase)

# Test case 2: Validate the function with large values
test_string_sequence(30)

# Test case 3: Validate the function with negative numbers
test_string_sequence(-10)

# Test case 4: Validate the function with large positive numbers
test_string_sequence(1000000)
```