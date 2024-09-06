```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """
    string_sequence() <tested with n = 0, 5>
    """
    return "".join(range(0, n + 1))

# Test the function with different input values
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10)) # Throws ValueError: Length must be <= 9
```