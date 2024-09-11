```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` (inclusive). The function uses the `range` function to generate the numbers and the `join` method to concatenate them into a string with spaces in between. The `map` function is used to convert each number to a string before joining them.