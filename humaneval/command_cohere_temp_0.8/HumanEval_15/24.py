```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the built-in `range()` function in Python which creates a sequence of numbers starting from 0 up to including `n` (the parameter passed in). The `map()` function is then used to convert these sequence of numbers into strings and `join()` is used to concatenate these strings into one string separated by spaces.