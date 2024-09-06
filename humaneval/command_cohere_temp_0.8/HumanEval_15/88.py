```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet uses the `range()` function to generate a sequence of numbers from 0 to `n`, inclusive. The resulting sequence is then converted to a string using `map()` and `str()` functions, and joined together with spaces using the `join()` method. The specified tests assert the function's behavior for 0 and 5 as input, but you can expand the test suite by examining various input cases.