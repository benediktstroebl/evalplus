```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A space-delimited string of numbers from 0 to n.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script, the `string_sequence` function uses a generator expression to create a sequence of numbers from 0 to `n` (inclusive) using the `range` function. The `map` function is used to convert each number to a string, and `' '.join(...)` is used to join these strings together with spaces in between.