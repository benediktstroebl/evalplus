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
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, `range(n + 1)` generates a sequence of numbers from 0 to n inclusive. The `map(str,...)` expression converts each number in the sequence to a string. Finally, `' '.join(...)` joins the strings together with spaces in between. The result is a string containing space-delimited numbers starting from 0 upto n inclusive.