```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n.

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

This script defines the `string_sequence` function as specified. It uses the built-in `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and the `map` function to convert these numbers to strings. The `' '.join(...)` expression then concatenates these strings into a single string with spaces in between.

The script also includes example usage and test cases to demonstrate its functionality.