```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit (inclusive) of the sequence.

    Returns:
        str: A string containing the space-delimited numbers of the sequence.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script uses a generator expression to generate the numbers from 0 to `n` (inclusive) and the `join()` method to concatenate them into a string with spaces in between. The expression `str(i) for i in range(n + 1)` generates the numbers, and `' '.join(...)` concatenates them with spaces. The `+ 1` in `range(n + 1)` is necessary to include `n` in the sequence.