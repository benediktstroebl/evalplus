```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))

# Example use cases:
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

This script defines the `string_sequence` function, which uses a generator expression to iterate over the numbers from 0 to `n` (inclusive), converts each number to a string, and joins them together with spaces in between. The `join` method is used to concatenate the strings. The function is then tested with the provided example use cases.