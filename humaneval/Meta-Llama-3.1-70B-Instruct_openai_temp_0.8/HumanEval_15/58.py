```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))


# Example usage:
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that generates a string of space-delimited numbers from 0 to `n` inclusive. The function uses a generator expression within the `join` method to create the desired string. The `+ 1` in `range(n + 1)` ensures that `n` is included in the sequence.