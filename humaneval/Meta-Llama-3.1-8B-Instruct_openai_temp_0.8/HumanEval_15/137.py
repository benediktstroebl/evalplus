```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

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
    return''.join(str(i) for i in range(n + 1))


# Test the function
print(string_sequence(0))   # Expected output: '0'
print(string_sequence(5))   # Expected output: '0 1 2 3 4 5'
print(string_sequence(10))  # Expected output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines a function `string_sequence(n)` that uses a generator expression to generate numbers from 0 to `n` (inclusive) and joins them into a string with spaces in between using `' '.join()`. The function is then tested with different inputs to demonstrate its correctness.