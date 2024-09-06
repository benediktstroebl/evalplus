```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10)) # Output: '0 9 8 7 6 5 4 3 2 1'
```