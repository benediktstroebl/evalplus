```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.

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

This script defines the `string_sequence` function which generates a string of space-delimited numbers from 0 to `n` (inclusive) and returns it. The example usage demonstrates how to use this function with inputs of 0 and 5. 

Note: The `join` method is used to concatenate the numbers into a string with spaces in between. `map(str, range(n + 1))` is used to convert the range of numbers to strings, so they can be joined together. The `+ 1` is necessary because `range` generates numbers up to but not including the stop value.