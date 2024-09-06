```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

# Test the function with different inputs
test_string_sequence(0)
test_string_sequence(1)
test_string_sequence(5)
test_string_sequence(10)
test_string_sequence(100)
```