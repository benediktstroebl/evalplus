### string_sequence Function
#### Generates a string with space-delimited numbers from 0 to n inclusive

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers from 0 to n inclusive.

    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


# Example usage
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This script defines the `string_sequence` function which takes an integer `n` as input. It uses a generator expression to generate a sequence of numbers from 0 to `n` (inclusive), and then joins these numbers into a string, separated by spaces. The function is then tested with example usage.