```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit for the sequence.

    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.

    Example:
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

In this script, the `string_sequence` function uses the `join` method to concatenate the numbers from 0 to `n` (inclusive) into a string, with spaces in between. The `map` function is used to convert each number to a string, so they can be joined together. The `range` function generates the numbers from 0 to `n`, and the `+ 1` is used to include `n` in the sequence.