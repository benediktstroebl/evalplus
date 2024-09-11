```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive.

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

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10)) # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This script defines the function `string_sequence` which generates a string containing space-delimited numbers from 0 to `n` inclusive. The function uses a generator expression to generate the numbers and the `join` method to concatenate them into a string with spaces in between. The upper limit of the sequence is included by adding 1 to `n` in the `range` function. The function is then tested with different inputs to demonstrate its correctness.