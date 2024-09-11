```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A space-delimited string containing numbers from 0 to n.
    
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
```

In this script, the `string_sequence` function uses a generator expression to generate the numbers from 0 to `n` (inclusive). The `join` method is then used to concatenate these numbers into a single string, with spaces between each number. The `range(n + 1)` part is used to ensure that the sequence includes `n`. 

The script also includes example use cases to demonstrate how the function works.