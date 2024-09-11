```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This Python script defines a function `string_sequence` that generates a string of space-delimited numbers from 0 to `n` inclusive. The `join` function is used to concatenate the numbers as strings with spaces in between. The `map` function is used to convert integers to strings. The `range` function generates numbers in the sequence.

The script includes test cases to verify its correctness.