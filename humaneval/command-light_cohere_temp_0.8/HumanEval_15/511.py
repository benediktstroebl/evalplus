```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different input values
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5' as expected)
print(string_sequence(1))  # Output: '1'
print(string_sequence(10)) # Output: '0000010'
print(string_sequence(100)) # Output: '000000100'
print(string_sequence(0, 2))  # Output: '00'
```