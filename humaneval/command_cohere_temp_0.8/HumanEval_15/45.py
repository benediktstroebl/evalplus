```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    return ' '.join(map(str, range(n+1)))

# Tests
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```