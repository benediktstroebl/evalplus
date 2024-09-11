```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))


# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that uses a generator expression to create a sequence of numbers from 0 to `n` (inclusive). The `join` function is then used to concatenate these numbers into a single string with space delimiters. The function includes a docstring that explains its purpose, parameters, and return value.