```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers.

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

This script defines the `string_sequence` function, which uses the `join` method and the `map` function to create a string containing the numbers from 0 to `n` inclusive, separated by spaces. The `range(n + 1)` expression generates the numbers in the sequence, and `map(str,...)` converts each number to a string so it can be joined with the others.