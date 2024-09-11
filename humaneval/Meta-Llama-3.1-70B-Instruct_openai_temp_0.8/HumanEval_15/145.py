```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(map(str, range(n + 1)))

# Example use cases:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, we use the built-in `range` function to generate a sequence of numbers from 0 to `n` (inclusive). We then use the `map` function to convert each number to a string. Finally, we use the `join` method to concatenate the strings with spaces in between.

You can run this script to test the `string_sequence` function with different inputs.