```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))


# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script uses a generator expression within the `join()` method to generate the sequence of numbers as strings and then join them together with spaces in between. The `range(n + 1)` function generates numbers from 0 up to `n` inclusive.