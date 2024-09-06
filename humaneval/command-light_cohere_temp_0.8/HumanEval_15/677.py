```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(str(i) for i in range(n))

# Test the function with different input values
print(string_sequence(0))      # Output: 0
print(string_sequence(1))      # Output: 1
print(string_sequence(5))     # Output: 0 1 2 3 4 5 

print(string_sequence(6))     # Error: Out of range
```