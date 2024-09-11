```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A space-delimited string of integers from 0 to n.

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

This script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `join()` method to concatenate the string representations of the numbers in the range, with spaces in between. The `map()` function is used to convert the integers in the range to strings. The `range(n + 1)` expression generates numbers from 0 to `n` inclusive.