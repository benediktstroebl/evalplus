```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script, we're using a generator expression within the `join` function to generate the sequence of numbers as strings. The `range(n + 1)` function generates a sequence of numbers from 0 up to `n` inclusive. The `' '.join()` function then concatenates these numbers into a single string with spaces in between.