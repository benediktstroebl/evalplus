```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with some inputs
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(string_sequence(-3), '0 0 0 0 0')
assertEqual(string_sequence(10), '0 9138 941 989 1000 10')
```