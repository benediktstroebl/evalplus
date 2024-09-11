```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script uses the built-in `range` and `map` functions in Python to generate the sequence of numbers from 0 to `n` (inclusive), convert each number to a string using `map`, and then join the resulting strings together with spaces in between using `' '.join()`. The `+ 1` in `range(n + 1)` is necessary because `range` generates numbers up to but not including the specified upper limit.