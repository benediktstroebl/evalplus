```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n inclusive.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script uses the built-in `join` function to concatenate the numbers in the sequence into a single string, with spaces in between. The `map` function is used to convert each number in the sequence to a string, so that they can be joined together. The `range` function generates a sequence of numbers from 0 to `n` inclusive.