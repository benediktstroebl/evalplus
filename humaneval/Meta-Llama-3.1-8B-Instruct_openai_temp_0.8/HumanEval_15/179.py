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
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This script defines a function `string_sequence` that uses the `join` method to concatenate a list of strings (the numbers from 0 to `n` inclusive) with spaces in between. The use of a generator expression (`str(i) for i in range(n + 1)`) ensures efficiency by avoiding creating an intermediate list. The `range(n + 1)` is used to include `n` in the sequence.