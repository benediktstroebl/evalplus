```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, the `string_sequence` function uses the `join` method to concatenate a sequence of numbers into a string, with spaces in between each number. The `map` function is used to convert each number to a string, and `range(n + 1)` generates the sequence of numbers from 0 to `n` inclusive.