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

# Example usage:
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
```

In this script, we define a function `string_sequence` that takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` inclusive. We use the `range` function to generate numbers from 0 to `n`, the `map` function to convert each number to a string, and the `join` function to concatenate these strings with spaces in between. The `+ 1` in `range(n + 1)` is necessary to include `n` itself in the sequence.

You can run this script and test the `string_sequence` function with different inputs.