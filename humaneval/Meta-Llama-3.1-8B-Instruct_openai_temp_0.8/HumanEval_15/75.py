```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

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
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function, which takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `join` method to concatenate the numbers together with spaces in between. The `map` function is used to convert each number to a string before joining them together. The `range(n + 1)` function generates a sequence of numbers from 0 to `n` inclusive. The test cases at the end demonstrate the function's behavior.