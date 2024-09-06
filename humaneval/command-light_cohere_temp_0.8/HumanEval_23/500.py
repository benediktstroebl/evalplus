```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

# Testing the function
>>> strlen('') # Output: 0
>>> strlen('abc')  # Output: 3
>>> strlen('') & 5   # Should return error
```