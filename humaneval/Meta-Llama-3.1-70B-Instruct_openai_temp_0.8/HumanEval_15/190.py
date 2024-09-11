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

# Example use cases:
print(string_sequence(0))   # Output: '0'
print(string_sequence(5))   # Output: '0 1 2 3 4 5'
```

In this script, we define a function `string_sequence` that uses the `range` function to generate numbers from 0 to `n` inclusive. The `map` function is used to convert these numbers to strings. Finally, the `join` function is used to concatenate these strings with a space separator.