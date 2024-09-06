```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` (inclusive) using the `range` generator and the `str` mapping function. The function is tested against two cases, and the assertions confirm the expected behavior.