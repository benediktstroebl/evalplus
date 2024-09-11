```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper bound of the sequence.

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
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This script defines a function `string_sequence` that generates a string of space-delimited numbers from 0 to `n` inclusive. The `range(n + 1)` function generates a sequence of numbers from 0 to `n`, and `map(str,...)` converts these numbers to strings. The `' '.join(...)` function then joins these strings with spaces in between to form the final output string. The script also includes some test cases to demonstrate the function's usage.