```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This approach uses the `range()` and `map()` functions to generate numbers up to the input `n` and then uses `str()` and `join()` to convert these numbers into a string with numerical values `n` through `0`. 

The `join()` method has the advantage of concatenating strings together in a chainable manner. In this scenario, it amalgamates the numerical values created by `range()` and `str()` into a single string.