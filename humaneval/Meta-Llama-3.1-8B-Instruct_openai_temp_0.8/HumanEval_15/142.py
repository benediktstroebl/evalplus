```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A space-delimited string of numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, we use the `join()` function to concatenate a list of strings into a single string, with spaces in between. The list of strings is generated using a generator expression that produces numbers from 0 to `n` (inclusive) using the `range()` function, and converts each number to a string using `str(i)`.