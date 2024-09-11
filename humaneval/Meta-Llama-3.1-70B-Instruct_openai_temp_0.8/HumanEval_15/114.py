```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Example usage
print(string_sequence(0))  # Outputs: '0'
print(string_sequence(5))  # Outputs: '0 1 2 3 4 5'
```

This script uses Python's built-in `range` function to generate numbers from 0 to `n` (inclusive), `map` to convert these numbers to strings, and `join` to concatenate them into a single string with spaces in between. The `+ 1` in `range(n + 1)` is necessary because `range` stops one number before the specified end.