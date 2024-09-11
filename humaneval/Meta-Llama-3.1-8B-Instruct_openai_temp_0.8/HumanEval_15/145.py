```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers from 0 to n.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))
print(string_sequence(5))
```

This script defines the `string_sequence` function, which takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The example usage demonstrates how to use the function. The `join` method is used to concatenate the numbers into a single string, with spaces in between. The `map` function is used to convert the numbers to strings, so that they can be concatenated with spaces.