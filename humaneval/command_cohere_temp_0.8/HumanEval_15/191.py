```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This script includes a function called `string_sequence` which takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` (inclusive) using the `range` generator and the `str` mapping function. The example usage and test cases demonstrate the function's behavior for different input values.