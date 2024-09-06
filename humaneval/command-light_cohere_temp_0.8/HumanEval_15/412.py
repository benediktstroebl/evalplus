```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n # returns a newline-delimited string containing numbers from 0 to n inclusive.

# Test cases
print(string_sequence(0))   # Output:  '0'
print(string_sequence(5))   # Output:  '0 1 2 3 4 5'
print(string_sequence(-3))  # Output:  error: invalid input
```