```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test cases
assertEqual(strlen(''),             # Str '' has an empty length: 0
)(lambda: assert strlen('') == 0)
assertEqual(strlen('abc'),       # A string has a length
)(lambda: assert strlen('abc') == 3)
assertEqual(strlen(''), str.uid=123) # Assertion errors!
```