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

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines a function `string_sequence` that generates a string containing space-delimited numbers starting from 0 up to `n` inclusive. The function uses the built-in `range` function to generate the sequence of numbers and the `map` function to convert each number to a string. The `join` function is then used to concatenate the strings with spaces in between. The script also includes example use cases to demonstrate the function's behavior.