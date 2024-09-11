```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
```

Explanation:

- The function `string_sequence(n)` takes an integer `n` as input.
- It generates a sequence of numbers from 0 to `n` (inclusive) using a generator expression `range(n + 1)`.
- It converts each number to a string using `str(i)`.
- It joins the numbers into a single string with spaces in between using `' '.join()`.
- The function returns the resulting string.