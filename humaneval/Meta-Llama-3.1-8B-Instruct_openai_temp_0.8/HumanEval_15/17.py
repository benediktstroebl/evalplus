### Problem Solution

Here's a Python function that generates a string containing space-delimited numbers from 0 to `n` inclusive:
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
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
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
This function uses the `join` method to concatenate the elements of a list into a string, with each number converted to a string using `map`. The `range` function generates numbers from 0 to `n` inclusive, and we add 1 to `n` to include `n` itself in the sequence.