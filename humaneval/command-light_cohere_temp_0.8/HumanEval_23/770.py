```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if string is empty"""
    return len(string) if string else 0

# Testing the function
>>> strlen('') <<< 0  # Should return 0
>>> strlen('abc') <<< 3  # Should return 3
```