```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the code uses Python's `range` function to generate a sequence of numbers up to `n` and then uses `str` and `map` to convert this sequence to a string, delimited by spaces.