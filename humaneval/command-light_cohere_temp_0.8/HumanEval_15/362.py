```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..."*
    return

# Test cases
test_string = string_sequence(5)
assert test_string == '0 1 2 3 4 5'
test_string = string_sequence(0)
assert test_string == '0'
test_string = string_sequence(-5)
assert test_string == ''
test_string = string_sequence(10)
assert test_string == '0 9 8 7 6 5 4 3 2 1'
```