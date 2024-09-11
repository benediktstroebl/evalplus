```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The end number of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers.
    
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Outputs: 0
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```

This script defines a function `string_sequence(n)` that returns a string containing space-delimited numbers from 0 to `n` inclusive. It uses the `join` function to concatenate the numbers with spaces in between. The `map(str, range(n + 1))` expression generates the numbers in the range from 0 to `n` (inclusive), converts them to strings, and passes them to the `join` function. 

The test cases at the end demonstrate how to use this function and verify its correctness.