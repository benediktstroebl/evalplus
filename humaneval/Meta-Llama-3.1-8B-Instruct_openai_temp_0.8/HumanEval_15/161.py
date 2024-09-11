```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers starting from 0 upto n inclusive.

    Example:
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

This script defines the `string_sequence` function as specified in the problem statement. The function uses the `join` method to concatenate the string representations of numbers from 0 to `n` (inclusive) with spaces in between. The `range` function is used to generate the sequence of numbers. The `map` function is used to convert the numbers to strings, which are then joined together. The script also includes test cases at the end to verify the function's correctness.