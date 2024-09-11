```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string of space-delimited numbers from 0 to `n`. The function uses the built-in `range` function to generate the sequence of numbers, `map` to convert each number to a string, and `join` to concatenate the strings into a single string with spaces in between.

The script also includes test cases to demonstrate the function's behavior for different inputs.