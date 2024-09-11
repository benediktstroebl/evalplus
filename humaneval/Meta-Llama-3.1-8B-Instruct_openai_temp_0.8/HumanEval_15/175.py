```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
```

In this script, we use the `join` method to concatenate the numbers in the sequence into a string. The `str(i)` is used to convert each number `i` to a string, and the `range(n + 1)` generates numbers from 0 to `n` inclusive.