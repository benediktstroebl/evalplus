```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
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

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script, the `string_sequence` function takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. It uses the `join` function to concatenate the numbers into a single string, and the `map` function to convert each number to a string before joining. The `range` function is used to generate the sequence of numbers. The test at the end of the script demonstrates the function's usage.