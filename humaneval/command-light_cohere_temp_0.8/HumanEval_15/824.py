```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n + 1) + "0}"

# Test the function with different values of n
test_string_sequence = string_sequence(0)
assert test_string_sequence == '0'
test_string_sequence = string_sequence(5)
assert test_string_sequence == '0 1 2 3 4 5'
```