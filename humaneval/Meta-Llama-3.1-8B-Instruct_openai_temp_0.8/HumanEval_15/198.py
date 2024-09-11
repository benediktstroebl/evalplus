```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))   # Output: 0
print(string_sequence(5))   # Output: 0 1 2 3 4 5
```

In this solution, we use the `join()` method to concatenate the string representation of numbers in the range from 0 to `n` (inclusive) with spaces in between. The generator expression `str(i) for i in range(n + 1)` generates the required numbers as strings.