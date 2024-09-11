```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. It uses the `join()` method to concatenate the numbers into a string, and `map(str, range(n + 1))` to convert the numbers to strings. The `range(n + 1)` generator produces numbers from 0 to `n`, and the `+ 1` accounts for the fact that the `range()` function is exclusive of the end value.