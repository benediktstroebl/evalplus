```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n inclusive.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

This Python script uses the `join` method to concatenate a list of strings into a single string, with spaces in between. The `map` function is used to convert the integers in the `range` object to strings, which can then be joined together. The `+ 1` in `range(n + 1)` is used to include `n` itself in the sequence.