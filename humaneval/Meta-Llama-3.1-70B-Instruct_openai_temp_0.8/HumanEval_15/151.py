```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence (inclusive).
    
    Returns:
    str: A string containing space-delimited numbers.
    
    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This Python script defines a function `string_sequence` that generates a string of space-delimited numbers from 0 to `n` (inclusive). It uses a generator expression to create the sequence of numbers and the `join` method to concatenate them into a single string.