```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` (inclusive). The function uses a generator expression inside the `join` method to generate the numbers and join them into a string. The `range(n + 1)` is used to include `n` in the sequence. The script then tests the function with two examples.