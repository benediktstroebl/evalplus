```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing the sequence of numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` inclusive. It uses the `range` function to generate the numbers, `map` to convert them to strings, and `join` to concatenate them with spaces in between. The test cases at the end verify that the function behaves as expected.