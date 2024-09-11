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
    
    # Use the map function to convert each number to a string and the join function to join them with spaces
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this code, we use the `range(n + 1)` function to generate a sequence of numbers from 0 to n (inclusive), and then we use the `map` function to convert each number to a string. Finally, we use the `join` function to join these strings with spaces.