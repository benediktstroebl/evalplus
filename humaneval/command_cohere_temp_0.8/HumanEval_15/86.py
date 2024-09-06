```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This approach uses the `range()` function to generate numbers up to the supplied `n` parameter, inclusive, and then maps these numbers to strings and joins them with spaces using the `join()` method. 

The problem is then simplified to directly return the resulting string. 

This approach is efficient and amenable to parallelization, as it involves a single linear pass to generate the sequence of numbers.