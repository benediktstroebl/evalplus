```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The end of the sequence.

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
print(string_sequence(0))  # Expected output: 0
print(string_sequence(5))  # Expected output: 0 1 2 3 4 5
```

This script defines a function `string_sequence` that generates a string sequence of numbers from 0 to `n` (inclusive) separated by spaces. It uses the `range` function to generate the numbers and `map` to convert them to strings. The `join` function is used to combine these strings into a single string with spaces in between. The script includes a docstring with examples to test the function.