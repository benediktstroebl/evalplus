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
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines the `string_sequence` function, which generates a sequence of numbers from 0 to `n` (inclusive) and returns them as a string with space-delimited numbers. The `range(n + 1)` generates numbers up to `n` (inclusive) because the upper limit in the `range` function is exclusive. The `map(str,...)` converts each number to a string, and the `' '.join(...)` joins these strings together with spaces in between.