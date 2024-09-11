### Python Script to Generate Space-Delimited Number Sequence

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
    # Use a list comprehension to generate the numbers and join them with spaces
    return''.join(str(i) for i in range(n + 1))


# Example usage:
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses a list comprehension to generate the numbers and the `join` method to concatenate them with spaces. The example usage demonstrates how to use the function with different inputs.