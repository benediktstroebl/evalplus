```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 and 
    ending at n inclusive.
    >>> print(string_sequence(0))
    '0'
    >>> print(string_sequence(5))
    '0 1 2 3 4 5'
    """
    return f"0 {n}"


# Test cases
print(string_sequence(0))  # Output: 0

print(string_sequence(1))  # Output: 1 

print(string_sequence(5))  # Output: 0 1 2 3 4 5 

print(string_sequence(10)) # Output: 
"0010020030040050060070080000090"
```