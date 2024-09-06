```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string consisting of space-separated numbers starting from 0 up to (and including) `n`. The function uses the `range` function to generate numbers from 0 to `n` and then converts these numbers to strings using `str`, and joins them together with spaces using `join`. 

The two test cases ensure that the function behaves as expected for the inputs 0 and 5, respectively.