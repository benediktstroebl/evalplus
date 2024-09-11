### String Sequence Generator

The following Python script defines a function `string_sequence` that generates a string containing space-delimited numbers from 0 to `n` inclusive.

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

In this script, the `string_sequence` function uses a generator expression to generate numbers from 0 to `n` inclusive. The `join` method is then used to concatenate these numbers into a string with spaces in between. The `+ 1` in `range(n + 1)` is necessary to include `n` in the sequence.