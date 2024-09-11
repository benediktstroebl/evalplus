```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string of space-delimited numbers from 0 to n.
    
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines a function `string_sequence(n)` that generates a string sequence from 0 to `n` inclusive, with each number separated by a space. The `join()` method is used to concatenate the numbers into a single string. The `range(n + 1)` function generates a sequence of numbers from 0 to `n`, and the `str(i)` function converts each number to a string.