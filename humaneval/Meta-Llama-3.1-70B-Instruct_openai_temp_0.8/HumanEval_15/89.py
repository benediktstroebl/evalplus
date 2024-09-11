```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Outputs: 0
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```

This script defines a function `string_sequence` that takes an integer `n` and returns a string of space-delimited numbers from 0 to `n` (inclusive). The `range` function generates numbers from 0 to `n`, and the `map` function converts these numbers to strings. Finally, the `' '.join()` method concatenates the strings into a single string with spaces in between.

You can run this script to test the `string_sequence` function with different inputs.