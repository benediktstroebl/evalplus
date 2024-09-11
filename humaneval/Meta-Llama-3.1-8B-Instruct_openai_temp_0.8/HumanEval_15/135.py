```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script uses the built-in `map` function in combination with the `join` method to generate the desired string sequence. The `range(n + 1)` function is used to generate numbers from 0 to n, inclusive. The `map(str,...)`, which maps each integer to a string, is then passed to `join` to concatenate them into a single string, separated by spaces.