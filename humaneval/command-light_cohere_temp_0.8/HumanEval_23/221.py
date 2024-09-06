```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test cases
>>> strlen('')
0

>>> strlen('abc')
3

>>> strlen('')
Traceback (most recent call last):
  File "<filename>", line 19, in <module>
Line 19:                strlen('')
    ^
  File "<filename>", line 6, in <string_defined_above>
Return of
AttributeError: 'str' object has no attribute 'strlen'

>>> strlen('A')
Traceback (most recent call last):
  File "<filename>", line 25, in <module>
Line 25:                strlen('A')
    ^

True
```