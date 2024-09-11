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

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` and returns a string of space-delimited numbers from 0 to `n` (inclusive). It uses the built-in `range` function to generate the sequence of numbers and the `map` function to convert each number to a string. The `join` method is then used to concatenate these strings into a single string with spaces in between.