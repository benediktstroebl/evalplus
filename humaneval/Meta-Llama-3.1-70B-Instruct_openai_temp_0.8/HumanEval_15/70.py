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

# Example use cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, the `string_sequence` function uses the built-in `range` function to generate numbers from 0 to `n` (inclusive), converts each number to a string using `map`, and then joins these strings with spaces using the `join` method.

You can run this script as is to see the example use cases in action.