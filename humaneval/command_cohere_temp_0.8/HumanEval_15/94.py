```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code defines a function called `string_sequence`, which takes an integer as an input and returns a string containing space-separated numbers starting from 0 up to including the input value `n`. The function uses the `range` function to generate a sequence of numbers from 0 to `n` and then uses the `join` method to join these numbers into a single string with spaces as separators. The behavior of the function is further illustrated by the provided tests, confirming its correctness.  This problem can also be solved using various Python f-strings.