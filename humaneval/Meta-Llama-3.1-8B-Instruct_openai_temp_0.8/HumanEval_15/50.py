```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers from 0 to n inclusive.

    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
```

This Python script defines a function `string_sequence` that generates a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `join` method to concatenate the numbers into a single string, and the `map` function to convert the numbers to strings. The script also includes test cases to demonstrate the function's behavior.