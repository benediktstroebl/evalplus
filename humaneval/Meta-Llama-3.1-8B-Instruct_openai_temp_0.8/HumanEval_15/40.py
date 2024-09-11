```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper bound of the sequence.
    
    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    
    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))  # Add 1 to include n in the sequence


# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script uses the `join()` function to concatenate the string representation of numbers from 0 to `n` into a single string, separated by spaces. The `map()` function is used to convert the range of numbers to strings before joining them.