```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n inclusive.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test the function
print(string_sequence(0))  # Should print: 0
print(string_sequence(5))  # Should print: 0 1 2 3 4 5
```

In this script, we define a function `string_sequence` that takes an integer `n` as input. Inside the function, we use a `map` function to convert each number from a range of numbers from 0 to `n` (inclusive) to a string, and then use the `join` method to concatenate these strings into a single string with spaces in between.