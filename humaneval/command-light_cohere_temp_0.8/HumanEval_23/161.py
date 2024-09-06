```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),       0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('1234')), 4
assertEqual(strlen('abc123')), 5
assertEqual(strlen(' ')), 0)
assertEqual(strlen('foo')), 6
assertEqual(strlen('abcXyz') , 7)
```