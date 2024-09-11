```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers from 0 to n (inclusive).
    
    Example:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` (inclusive). The function uses a generator expression to generate the numbers, `join` to concatenate them into a string, and `str(i)` to convert each number to a string. The `+ 1` in `range(n + 1)` ensures that `n` is included in the sequence. The example usage at the end demonstrates how to call the function with different inputs.