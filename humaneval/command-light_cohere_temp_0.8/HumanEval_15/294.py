```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with various values of n
test_string_sequence = string_sequence(0)
assertEqual(test_string_sequence, '0')
test_string_sequence = string_sequence(5)
assertEqual(test_string_sequence, '0 1 2 3 4 5')
```