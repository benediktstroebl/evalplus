```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."  # list comprehension with string concatenation and formatting

# Test cases
 assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
assert string_sequence(10) == '0 9 8 7 6 5 3 2 1 0'
assert string_sequence(21) == '0 20 19 18 17 16 15 14 13 10 9 8'
```