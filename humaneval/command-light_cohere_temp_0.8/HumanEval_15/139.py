```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

# Test case 1
test_str = string_sequence(0)
assert test_str == '0'

# Test case 2
test_str = string_sequence(5)
assert test_str == '0 1 2 3 4 5'

# Test case 3 - Should throw an error
try:
    string_sequence(-1)
except TypeError:
    print("Test case 3 should have thrown an error")
```