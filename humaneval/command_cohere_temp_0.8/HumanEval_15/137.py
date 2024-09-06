```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the function uses the `range()` and `map()` functions to generate numbers up to `n` and convert them to strings, respectively. The `join()` function is then used to concatenate the strings with spaces in between.