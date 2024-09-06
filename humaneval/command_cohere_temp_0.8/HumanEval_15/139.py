```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code defines a function called `string_sequence`, which takes an integer n as input and returns a string consisting of space-separated numbers ranging from 0 to n inclusive. The function uses the `range` function to generate an iterable of numbers from 0 to n (inclusive) and then maps each number to a string using the `str` function. The joined string is returned as the result.

The tests assert that the function behaves as expected for two different input values.