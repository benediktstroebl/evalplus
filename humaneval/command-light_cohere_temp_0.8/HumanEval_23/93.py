```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with a string containing only spaces
>>> strlen('')
# Should return 0
True

# Test the function with a longer string
>>> strlen('abc')
# Should return 3
True

# Test with an empty string
>>> strlen('')
# Should return 0
True

# Test with a string starting with a number
>>> strlen('10')
# Should return 0
True
```