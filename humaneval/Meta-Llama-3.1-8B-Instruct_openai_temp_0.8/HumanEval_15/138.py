```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

print(string_sequence(0))
print(string_sequence(5))
```

This script uses the `range(n + 1)` function to generate a sequence of numbers from 0 to `n` (inclusive), and then uses the `map` function to convert each number to a string. The `join` function is used to concatenate these strings into a single string with spaces in between.