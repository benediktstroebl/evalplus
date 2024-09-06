```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive."""
    return ("".join(f"0 {n}") * n)

# Test the function with different inputs
assertEqual(string_sequence(0), "0")
assertEqual(string_sequence(1), "0 1")
assertEqual(string_sequence(5), "0 1 2 3 4 5")
assertEqual(string_sequence(10), "0 9 8 7 6 5 4 3 2 1")
assertEqual(string_sequence(77), "0 77 76 65 43 19 12 6 4 3 2 1")
```