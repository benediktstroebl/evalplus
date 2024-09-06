```python
def string_sequence(n: int) -> str:
    return f" {0} {1} {2} {3} {4} {5}" * n

# Test the function with different inputs
assertEqual(string_sequence(0),'0')
assertEqual(string_sequence(5),'0 1 2 3 4 5')
assertEqual(string_sequence(-5),'0 0 0 0 0')
assertEqual(string_sequence(10),'0 9  9  9  9 10')
assertEqual(string_sequence(0),'0')
```