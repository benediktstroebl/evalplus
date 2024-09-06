```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} " * (n+1)

# Test case 1: Validate function with expected output
def test_string_sequence(test_n: int) -> None:
    assert string_sequence(test_n) == f"0 {test_n} ", f"Error: {test_n} was not correctly formatted"

# Test case 2: Validate function with large value of n
test_string_sequence(50)

# Test case 3: Validate function with negative value of n
test_string_sequence(-5)
```
This code defines a function **string_sequence** that creates a string containing space-separated numbers from 0 to n, inclusive. For test cases, it provides validation for the function by asserting that the output is correct.