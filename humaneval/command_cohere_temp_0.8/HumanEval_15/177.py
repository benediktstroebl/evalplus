```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that returns a string with `n+1` space-separated numbers starting from `0`. It uses the `range()` and `map()` functions to generate an array of numbers from `0` to `n` and then uses `str()` to convert each number into a string and `join()` to concatenate the strings with spaces in between.

The `string_sequence()` function is tested with two test cases: `n = 0` and `n = 5`. In both cases, the function's output is validated against the expected output.