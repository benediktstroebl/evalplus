```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 2 3 4 5 {n}"

# Test cases
print(string_sequence(0)) # Output: 0 

print(string_sequence(1)) # Output: 01 

print(string_sequence(5)) # Output: 0105 

print(string_sequence(10)) # Output: 0101010101 

```