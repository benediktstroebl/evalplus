```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),            0)
assertEqual(strlen('')),         0
assertEqual(strlen('abc')),   3
assertEqual(strlen('abcabc')), 6)
assertEqual(strlen('')),         0
assertEqual(strlen('    ')),    0
assertRaises(TypeError, strlen,' 'foo')
```