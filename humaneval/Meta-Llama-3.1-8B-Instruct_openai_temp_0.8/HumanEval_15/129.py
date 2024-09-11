```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing the numbers as a space-delimited sequence.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that uses the `range()` function to generate numbers from 0 to `n` (inclusive), converts them to strings using `map()`, and then joins them together into a single string with spaces in between using the `join()` function. The result is a string containing the numbers as a space-delimited sequence.