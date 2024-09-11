```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers starting from 0 up to n.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


# Example use cases
print(string_sequence(0))
print(string_sequence(5))
```

In this script, the `string_sequence` function generates a sequence of numbers from 0 to `n` (inclusive) and joins them into a single string with spaces in between. The `join` method is used to concatenate the string representations of the numbers with spaces in between. The `range` function is used to generate the sequence of numbers.