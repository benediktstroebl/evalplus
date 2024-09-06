```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This script includes a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-separated numbers starting from 0 up to (and including) `n`. The function uses the `range()` and `map()` functions to generate numbers up to `n` and convert them to strings, and the `join()` method to join these strings into one string with spaces in between.

The tests check if the function behaves as expected for 0 and 5 as input and demonstrate its behavior through printed outputs of the function calls.