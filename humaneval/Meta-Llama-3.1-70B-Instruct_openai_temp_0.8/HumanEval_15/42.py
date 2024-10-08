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
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

In this script, we use a generator expression to generate numbers from 0 to `n` (inclusive) and convert them to strings. The `' '.join(...)` function is then used to concatenate these strings with spaces in between. The `range(n + 1)` function is used to include `n` in the sequence.