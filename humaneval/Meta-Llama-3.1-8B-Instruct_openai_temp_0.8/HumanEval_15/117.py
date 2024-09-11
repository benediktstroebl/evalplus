### Solution

```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A space-delimited string of numbers from 0 to n.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
```

This script uses the built-in `range` function to generate numbers from 0 to `n` (inclusive) and `map` to convert these numbers to strings. The `join` function is then used to concatenate these strings with spaces in between.