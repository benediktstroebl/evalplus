```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.

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

This script defines a function `string_sequence(n)` that generates a string of space-delimited numbers from 0 to `n` (inclusive). It uses the `join()` function and a generator expression to convert each integer in the range to a string and join them together with spaces in between. The `map()` function is used to apply the `str()` function to each number in the range. The `range(n + 1)` function generates the numbers from 0 to `n` (inclusive).