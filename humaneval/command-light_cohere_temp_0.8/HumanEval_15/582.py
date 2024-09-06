```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n inclusive"""
    return f"0 {n} 0"

# Test the function with different values
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(string_sequence(-1), '0 0')
assertEqual(string_sequence(100), '0 99 98 97 96 95 00')
assertEqual(string_sequence(202), '0 200 201 201 200 201 200')
```