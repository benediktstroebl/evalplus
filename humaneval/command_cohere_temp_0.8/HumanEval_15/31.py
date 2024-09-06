```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This version of the `string_sequence` function uses the `range` generator function and the `map` function to generate a list of numbers from 0 to `n` (inclusive), and then joins these numbers into a single string with spaces as the delimiter. The `str` function is used to convert the integer numbers to strings.