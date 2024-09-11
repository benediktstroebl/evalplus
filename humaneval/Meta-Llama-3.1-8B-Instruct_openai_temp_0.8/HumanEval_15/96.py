```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

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
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function `string_sequence` that generates a string of space-delimited numbers from 0 to `n` inclusive. It uses the `map` function to convert the numbers to strings, and then joins them with spaces using the `join` method. The script also includes test cases to demonstrate the function's behavior.