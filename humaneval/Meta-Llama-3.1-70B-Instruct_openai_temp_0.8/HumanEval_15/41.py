```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```
This script defines the `string_sequence` function, which takes an integer `n` and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `range` function to generate the sequence of numbers, the `map` function to convert the numbers to strings, and the `join` function to concatenate the strings with spaces in between. The example usage demonstrates how to call the function with different inputs.