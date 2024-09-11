```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing the sequence of numbers.
    """
    return''.join(str(i) for i in range(n + 1))


# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing the numbers from 0 to `n` inclusive, separated by spaces. The `join` method is used to concatenate the numbers into a single string, and a generator expression is used to generate the numbers. The `range` function generates numbers up to `n + 1` to include `n` in the sequence.