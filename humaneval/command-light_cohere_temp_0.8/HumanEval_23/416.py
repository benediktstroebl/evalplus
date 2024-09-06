```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test cases
assertEqual(strlen(''),   0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('   '), 1)
assertEqual(strlen('abcabc'), 6)
assertEqual(strlen('abcabcab'), 6)
```