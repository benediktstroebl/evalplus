```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))


# Example use cases:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function, which takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` inclusive. It uses a generator expression within the `join` function to efficiently generate the sequence and format it as a string. The example use cases at the end demonstrate how to use this function with different inputs.