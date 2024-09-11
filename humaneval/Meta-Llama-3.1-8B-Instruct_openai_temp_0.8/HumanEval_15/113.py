```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.

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

This script defines a function `string_sequence(n)` that generates the required string sequence. It uses the `join()` method to concatenate the numbers from 0 to `n` (inclusive) with spaces in between. The `map()` function is used to convert the numbers to strings, which is necessary for the `join()` method to work correctly. The `range(n + 1)` function generates a sequence of numbers from 0 to `n` inclusive, and the `+ 1` is used to include `n` in the sequence.