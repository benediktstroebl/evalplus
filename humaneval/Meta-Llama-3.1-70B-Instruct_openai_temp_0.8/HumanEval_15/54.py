```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string of space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
```

In this script, the `string_sequence` function uses the built-in `range` function to generate a sequence of numbers from 0 to `n` (inclusive). The `map` function is then used to convert these numbers to strings, and finally, the `join` function is used to concatenate these strings into a single string with spaces in between.