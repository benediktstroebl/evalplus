```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
>>> string_sequence(0)
'0'

>>> string_sequence(5)
'0 1 2 3 4 5'
```

The `string_sequence` function uses the `range()` and `map()` functions to generate a list of numbers from 0 to `n` (inclusive), and then joins these numbers into a single string with spaces as the delimiter. 

The example usage and test cases demonstrate that the function produces the expected results.  This approach provides a concise solution in a single function, making it both self-contained and easy to understand.