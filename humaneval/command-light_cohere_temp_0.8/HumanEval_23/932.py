Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('']), 0)
assertEqual(strlen('    '), 4)
```