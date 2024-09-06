```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```

The `string_sequence` function uses the `range` function to generate a list of numbers from 0 to `n` (inclusive), and then uses the `join` method to convert this list into a single string with spaces as separators. 

The example usage provided in the docstring shows that the function correctly handles `n` values of 0 and 5, returning the expected results.