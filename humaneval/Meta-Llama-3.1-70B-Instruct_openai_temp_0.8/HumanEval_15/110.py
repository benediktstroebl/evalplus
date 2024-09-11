```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string of space-delimited numbers from 0 to n.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Outputs: 0
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```

This script uses the built-in `range` function to generate a sequence of numbers from 0 to `n` (inclusive), then uses the `map` function to convert each number to a string. Finally, it uses the `join` method to combine the strings into a single string with space delimiters.