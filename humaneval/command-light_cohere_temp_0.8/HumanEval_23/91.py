```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test cases
assertEqual(strlen(''),            0)
assertEqual(strlen('abc')), 3)
assertEqual(strlen(' galvanised iron')), 11  # Should be 12
assertEqual(strlen(' '),         0) # Empty string is 0
```