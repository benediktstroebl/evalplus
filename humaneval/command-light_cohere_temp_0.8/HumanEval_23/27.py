Here's the solution:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Test case for empty string
assertEqual(strlen(''), 0)

# Test case for only spaces
assertEqual(strlen(' '), 0)

# Test case for normal string
assertEqual(strlen('abc'), 3)

# Test case for lowercase characters only
assertEqual(strlen('abc'), 3)

# Test case for special characters too
assertEqual(strlen(@#[abc]), 3)
```