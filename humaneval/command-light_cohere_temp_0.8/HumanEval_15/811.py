```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2}...{n} "

# Test the function with different inputs
assert(string_sequence(0) == '0'),(string_sequence(1) == '1'),(string_sequence(5) == '0 1 2 3 4 5')
```