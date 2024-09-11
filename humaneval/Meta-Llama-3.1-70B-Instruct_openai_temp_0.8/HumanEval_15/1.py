```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The end of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Example use cases:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function, which generates a string of space-delimited numbers from 0 to `n` (inclusive) using a generator expression within the `join` method. The `range(n + 1)` function generates numbers up to `n` because the `range` function stops one number before the specified end.