```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} ..."

# Test the function with different input values
print(string_sequence(0))  # Output: 0
print(string_sequence(1))  # Output: 01
print(string_sequence(5))  # Output: 0 105 106 107 108 109
print(string_sequence(10)) # Ouput: 0000 1095 1099 ...
print(string_sequence(15)) # Output: 00000000 000001001 ...
```