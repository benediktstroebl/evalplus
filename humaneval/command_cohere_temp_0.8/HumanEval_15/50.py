```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This script defines a function called `string_sequence`, which takes an integer `n` as input and returns a string consisting of space-separated numbers ranging from 0 to `n` inclusive. The function uses the `range` function to generate a sequence of numbers from 0 to `n` and then uses the `map` function to convert these numbers to strings. Finally, the `join` function is applied to concatenate the strings into one sentence.

The function is encapsulated with a docstring that provides clear documentation, outlining its purpose, input, and output. This helps understand the function's intended behavior without having to inspect the source code.

The tests present in the script illustrate the behavior of `string_sequence` with different inputs and assert that the returned values conform to the expected output. You can use these tests to verify that the function behaves as expected.