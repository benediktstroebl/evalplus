```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Parameters:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string of space-delimited numbers.
    
    Example:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines a function `string_sequence(n)` that generates a string of space-delimited numbers from 0 to `n` inclusive. The `join()` function is used to concatenate the numbers into a single string, and the `map()` function is used to convert the integers into strings before joining them. The script also includes some error checking to ensure that the input is an integer.