```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence (inclusive).
    
    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))
print(string_sequence(5))
```

This Python script defines a function `string_sequence(n)` that generates a string containing space-delimited numbers starting from 0 up to and including `n`. It uses the `join` method to concatenate the numbers into a string, where each number is converted to a string using the `str` function. The `range` function generates the sequence of numbers, and `map` applies the `str` function to each number. The script also includes test cases to verify the function's correctness.