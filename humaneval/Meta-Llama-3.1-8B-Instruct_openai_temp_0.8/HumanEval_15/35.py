```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A string containing space-delimited numbers from 0 to n inclusive.
    
    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses a generator expression to generate the numbers, converts them to strings using the `str` function, and joins them together with spaces using the `join` method. The example usage shows how to call the function with different inputs and print the results.