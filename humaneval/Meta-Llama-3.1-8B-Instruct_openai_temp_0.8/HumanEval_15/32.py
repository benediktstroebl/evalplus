```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

Explanation:

*   The function `string_sequence(n)` generates a sequence of numbers from 0 to `n` (inclusive) using the `range` function.
*   The `map` function applies the `str` function to each number in the sequence, converting them to strings.
*   The `' '.join(...)` expression joins the strings with spaces in between, creating the final output string.