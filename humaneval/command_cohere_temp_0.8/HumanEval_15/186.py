```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This script defines a function called `string_sequence` that takes an integer `n` as input and returns a string containing a sequence of numbers from 0 to `n` separated by spaces. It uses the `range` function to generate an iterator of numbers up to `n` and converts it to a string using the `join` method. The example usage and test cases demonstrate the expected behavior of the function.