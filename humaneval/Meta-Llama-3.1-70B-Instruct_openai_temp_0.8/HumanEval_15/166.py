```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The last number in the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function as per the given problem statement. The function uses a generator expression to iterate over the numbers from 0 to `n` (inclusive) and converts each number to a string. The `join` method is then used to concatenate these strings with a space in between each number.

You can save this script to a file (e.g., `sequence.py`) and run it using Python (e.g., `python sequence.py`) to test the function.