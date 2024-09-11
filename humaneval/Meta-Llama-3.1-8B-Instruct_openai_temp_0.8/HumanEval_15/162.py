```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines the `string_sequence` function, which takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The `join` method is used to concatenate the numbers into a string. The example usage demonstrates the function's behavior with different inputs.