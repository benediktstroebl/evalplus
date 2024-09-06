```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the code uses Python's powerful `range` and `map` functions in conjunction with Python strings' versatile `join` function to produce the desired string sequence, all without needing any additional utilities. This maintains the simplicity, efficiency, and clarity of the code without relying on external modules.