```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string of space-separated numbers from 0 to n.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

In this script, the `string_sequence` function uses the built-in `range` function to generate a sequence of numbers from 0 to `n` (inclusive). The `map` function is then used to convert each number to a string. Finally, the `join` method concatenates these strings with spaces in between, resulting in the desired output. The test cases at the end verify the function's correctness.