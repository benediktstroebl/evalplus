```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers starting from 0 upto n inclusive.

    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 upto `n` inclusive. The function uses the `range` function to generate a sequence of numbers from 0 to `n` and the `map` function to convert these numbers to strings. The `join` method is then used to concatenate these strings with spaces in between. The script includes doctest-style comments to test the function with the provided examples.