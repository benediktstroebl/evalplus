```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
print(string_sequence(10))  # Expected output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines a function `string_sequence(n)` that takes an integer `n` as input. It uses a generator expression to generate a sequence of numbers from 0 to `n` (inclusive) and joins them together into a string with spaces in between using the `' '.join()` method. The function then returns this string.

The example use cases in the docstring demonstrate how to call the function with different inputs and verify that it produces the expected output.