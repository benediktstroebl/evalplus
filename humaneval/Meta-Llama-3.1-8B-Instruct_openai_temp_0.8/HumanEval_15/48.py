```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

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
    return''.join(str(i) for i in range(n + 1))


# Test the function
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function `string_sequence` that takes an integer `n` as input, generates a sequence of numbers from 0 to `n` (inclusive) using a generator expression, and joins them into a string with spaces in between using the `join` method. The function returns this string. The script also includes two test cases to demonstrate the function's behavior.