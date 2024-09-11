```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
```

This script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The `join()` function is used to concatenate the numbers into a string, and `map(str, range(n + 1))` is used to convert the numbers into strings.

Note that the `+ 1` in `range(n + 1)` is necessary because the `range()` function generates numbers up to but not including the specified end value. By adding 1 to `n`, we ensure that the sequence includes `n` itself.