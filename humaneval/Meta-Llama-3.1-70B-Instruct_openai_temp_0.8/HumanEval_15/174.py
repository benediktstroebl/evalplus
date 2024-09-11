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

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script, the `string_sequence` function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive), converts each number to a string using the `map` function, and then joins these strings together with spaces in between using the `join` method. The result is a string containing space-delimited numbers from 0 to `n`.