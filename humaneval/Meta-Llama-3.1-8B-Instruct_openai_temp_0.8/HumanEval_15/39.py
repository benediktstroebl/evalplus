```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # Expected output: '0'
print(string_sequence(5))  # Expected output: '0 1 2 3 4 5'
```

This script defines the `string_sequence` function, which generates a string of space-delimited numbers from 0 to `n` inclusive. The `join` function is used to concatenate the numbers into a single string, with spaces in between. The `map` function is used to convert each number to a string, so that they can be joined together.

The test cases at the end of the script demonstrate the function's behavior for different inputs.