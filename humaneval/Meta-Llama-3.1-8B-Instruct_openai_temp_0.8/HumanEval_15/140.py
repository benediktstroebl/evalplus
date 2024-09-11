```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines the `string_sequence` function which takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` inclusive. The `range(n + 1)` function generates a sequence of numbers from 0 to `n`, and the `map(str,...)` function converts these numbers to strings. The `' '.join(...)` function then joins these strings together with spaces in between. The script also includes some example usage of the function for testing.