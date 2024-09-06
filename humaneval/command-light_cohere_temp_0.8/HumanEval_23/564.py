```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test the function
# Ensure empty string returns 0
assert strlen('') == 0

# Test with different input
# Should return the length of the string
# 'abc'
assert strlen('abc') == 3
```