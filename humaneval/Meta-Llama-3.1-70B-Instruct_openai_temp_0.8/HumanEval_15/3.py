```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))   # '0'
print(string_sequence(5))   # '0 1 2 3 4 5'
print(string_sequence(10))  # '0 1 2 3 4 5 6 7 8 9 10'
```

In this script, we use the built-in `range` function to generate numbers from 0 to `n` (inclusive), `map` function to convert these numbers to strings, and `join` method to concatenate them into a single string with spaces in between. The `+ 1` in `range(n + 1)` is used to include `n` in the sequence.