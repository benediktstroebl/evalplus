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
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

In this script, we define the `string_sequence` function that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The `join` method is used to concatenate the numbers into a single string, and the `range` function generates the sequence of numbers. The `+ 1` in `range(n + 1)` is necessary to include `n` in the sequence.