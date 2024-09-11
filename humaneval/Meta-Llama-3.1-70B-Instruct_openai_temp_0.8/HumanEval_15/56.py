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
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function, which uses the `range` function to generate numbers from 0 to `n` (inclusive), converts these numbers to strings using `map`, and then joins them together with spaces in between using `' '.join()`. The function includes docstrings for documentation and clarity. Finally, two test cases are provided to demonstrate the function's usage.