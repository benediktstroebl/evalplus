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
This script defines a function `string_sequence` that takes an integer `n` as input, generates a sequence of numbers from 0 to `n` using the built-in `range` function, converts each number to a string using `map(str,...)`, and then joins these strings with spaces using `' '.join(...)`. Finally, it includes two example use cases to demonstrate the function's usage.