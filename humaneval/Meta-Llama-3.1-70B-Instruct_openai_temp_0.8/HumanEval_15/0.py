```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        str: A string containing the sequence of numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Example use cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script uses a generator expression to generate the numbers from 0 to `n` (inclusive), converts each number to a string, and then joins these strings together with spaces in between. The `range` function generates numbers up to `n` (inclusive) by specifying `n + 1` as the end value.