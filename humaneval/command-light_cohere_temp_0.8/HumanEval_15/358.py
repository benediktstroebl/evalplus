```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}" * (n + 1)

# Test the function with different values for n
test_string_sequence = string_sequence.assertEqual(0)
test_string_sequence # Output: '0'
test_string_sequence(5)
# Output: '0 1 2 3 4 5'
test_string_sequence(0)
# Output: ''
test_string_sequence(-1)
# Output: Traceback (most recent call last):
    ...
test_string_sequence(10)
# Output: Traceback (most recent call last):
    ...
```