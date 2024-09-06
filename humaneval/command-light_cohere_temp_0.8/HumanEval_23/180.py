```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with some strings
assertEqual(strlen(''),       0)
assertEqual(strlen(' ')),     0
assertEqual(strlen('abc')), 3
assertEqual(strlen('101')), 4

# Using the function:
assertEqual(strlen(''),       0)
assertEqual(strlen('abc')), 3
```