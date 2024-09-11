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


# Example usage
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

This script defines the `string_sequence` function to generate a string containing space-delimited numbers from 0 to `n` (inclusive) using the `join` function and the `range` function. The `map` function is used to convert each number in the range to a string before joining them. The example usage demonstrates how to call this function with different values of `n`.