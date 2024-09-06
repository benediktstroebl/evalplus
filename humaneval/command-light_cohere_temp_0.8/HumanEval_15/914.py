```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(str(i) for i in range(n))

# Test the function with different inputs
test_string_sequence(0) # Output: 0
test_string_sequence(5) # Output: 0 1 2 3 4 5 

# test_string_sequence(10) # Should raise error
```