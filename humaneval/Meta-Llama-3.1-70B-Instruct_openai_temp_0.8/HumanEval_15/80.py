```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The end value of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))


# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This Python function `string_sequence` uses a generator expression within the `join` method to create a string of space-separated numbers from 0 to the input number `n`. The `range(n + 1)` generates numbers from 0 to `n` inclusive, which are then converted to strings using `str(i)` and joined together with spaces in between.