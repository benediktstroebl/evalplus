```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}{' ' * (n-1)}"

# Test the function with n = 0
test_string_sequence(0)  # Should return '0'

# Test the function with n = 5
test_string_sequence(5)  # Should return '0 1 2 3 4 5'
```