```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers from 0 to n inclusive.
    
    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
In this script, the `string_sequence` function uses the `join` method to concatenate a list of strings into a single string. The `map` function is used to convert each number in the range to a string before joining them. The `range(n + 1)` function generates numbers from 0 to n inclusive.