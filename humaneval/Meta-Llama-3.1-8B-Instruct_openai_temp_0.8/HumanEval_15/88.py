```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

In this script, the `string_sequence` function uses a generator expression to generate numbers from 0 to `n` (inclusive), converts each number to a string, and joins them together with spaces using the `join` method. The `range(n + 1)` is used to include `n` in the sequence. The script then tests the function with two examples.