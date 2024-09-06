```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single integer argument labeled `n`. This function utilizes the `range` generator and `map` function to convert numbers from 0 to `n` into strings and then joins these strings together with spaces to form the desired string sequence.

The `string_sequence` function is purposely designed to generate a string that encompasses the aforementioned numbers, offering a clear and concise way to create sequences on demand. For instance, if you input `n = 5`, the function output would be `'0 1 2 3 4 5'`, which is precisely the intended sequence.