```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}"*n

# Test the function with some inputs
print(string_sequence(0))  
print(string_sequence(5))  
```