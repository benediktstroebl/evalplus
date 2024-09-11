```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

In this code:

*   We define a function `string_sequence(n)` that takes an integer `n` as input.
*   The function uses a generator expression to generate a sequence of numbers from 0 to `n` (inclusive).
*   We use the `join()` method to concatenate these numbers into a string, with spaces in between each number.
*   The example usage demonstrates how to call the function with different values of `n`.