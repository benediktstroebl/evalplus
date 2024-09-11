```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `join()` method to concatenate the numbers into a single string, and `map(str, range(n + 1))` to convert the numbers into strings. The `range(n + 1)` function generates numbers from 0 to `n` inclusive. The test cases at the end demonstrate the function's usage and behavior.