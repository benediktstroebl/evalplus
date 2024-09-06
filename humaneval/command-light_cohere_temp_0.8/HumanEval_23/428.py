```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1: empty string
assertEqual(strlen(''), 0)

# Test case 2: only alphabetic string
assertEqual(strlen('abc'), 3)
```