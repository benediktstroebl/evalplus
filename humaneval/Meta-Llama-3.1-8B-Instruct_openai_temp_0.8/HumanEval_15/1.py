```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))
print(string_sequence(5))
```

This script uses a generator expression to generate numbers from 0 to n (inclusive), converts each number to a string, and then joins them together with spaces in between using the `join()` method. The result is a string containing space-delimited numbers starting from 0 up to n inclusive.