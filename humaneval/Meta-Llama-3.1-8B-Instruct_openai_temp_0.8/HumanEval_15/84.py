```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers from 0 to n.
    
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This script defines a function `string_sequence(n)` that returns a string containing space-delimited numbers from 0 to `n` (inclusive). The function uses the built-in `range` function to generate numbers from 0 to `n` and `map` to convert these numbers to strings. The `join` method is then used to concatenate these strings with spaces in between. The script includes example usage to demonstrate how to call the function and display its output.