```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string of space-delimited numbers from 0 to n inclusive.
    
    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
print(string_sequence(10))  # Expected output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string of space-delimited numbers from 0 to `n` inclusive. The function uses a generator expression to generate the numbers and the `join` method to concatenate them into a string. The script includes docstrings to provide documentation for the function and test cases to verify its correctness.