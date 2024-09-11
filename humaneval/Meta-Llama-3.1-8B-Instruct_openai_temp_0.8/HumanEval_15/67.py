```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
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
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This script defines a function called `string_sequence` that generates a string containing space-delimited numbers from 0 to `n` inclusive. It uses a generator expression to generate the numbers, converts each number to a string, and joins them together with spaces using the `join` method. The function is then tested with different inputs to demonstrate its correctness.