```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script uses the `join()` function in combination with `map()` to convert each number in the `range()` to a string, and then join them together with spaces in between. The `+ 1` in `range(n + 1)` is used to include `n` in the sequence.