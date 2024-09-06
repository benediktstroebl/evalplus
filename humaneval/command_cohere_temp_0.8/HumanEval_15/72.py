```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single integer argument `n`. This function utilizes the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and employs the `str` module to convert these numbers into strings. The `join` function is then used to concatenate these strings together into one string, separated by spaces, and finally, this result is returned.

The `string_sequence` function is designed to create a string that represents a sequence of numbers from 0 up to, and including, a given number n. For example, if you call `string_sequence(5)`, it will return the string `'0 1 2 3 4 5'`, indicating the numbers from 0 to 5.