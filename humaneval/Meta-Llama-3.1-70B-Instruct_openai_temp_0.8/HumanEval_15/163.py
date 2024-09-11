```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This Python script defines a function `string_sequence(n)` that takes an integer `n` and returns a string of space-delimited numbers from 0 to `n` (inclusive). The `range(n + 1)` generates a sequence of numbers from 0 to `n`, `map(str,...)` converts these numbers to strings, and `' '.join(...)` concatenates them into a single string with spaces in between.

The script also includes example usage to demonstrate the function's behavior.