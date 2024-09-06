```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}" * (n + 1)

# Test the function with different inputs
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(1), '1')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(string_sequence(6), '0 1 2 3 4 5 6')
assertEqual(string_sequence(-1), '') # Test for negative value input
```