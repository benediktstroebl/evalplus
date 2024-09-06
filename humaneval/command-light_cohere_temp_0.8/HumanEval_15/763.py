```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 0" * (n + 1)

#Test cases
print(string_sequence(0))
print(string_sequence(5))
print(string_sequence(-5))
print(string_sequence(10))
print(string_sequence(0))
print(string_sequence(9))
```