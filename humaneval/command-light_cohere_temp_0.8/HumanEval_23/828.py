```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if the string is empty."""
    return len(string) if string else 0

# Test case 1: empty string
>>> strlen('')
0

# Test case 2: only char
>>> strlen('abc')
3
```