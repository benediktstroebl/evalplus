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
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that generates a string sequence of numbers from 0 to `n` (inclusive) separated by spaces. It uses the `range` function to generate the numbers and the `map` function to convert them to strings. The `join` method is then used to concatenate these strings with spaces in between.

The script also includes example usage of the function, which demonstrates how to call it with different inputs and print the resulting sequences.