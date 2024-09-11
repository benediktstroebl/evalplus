```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
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
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function as specified. The function uses the built-in `range` function to generate numbers from 0 to `n` (inclusive), converts them to strings using the `map` function, and then joins them together with spaces in between using the `join` method. The test cases at the end verify that the function works correctly.