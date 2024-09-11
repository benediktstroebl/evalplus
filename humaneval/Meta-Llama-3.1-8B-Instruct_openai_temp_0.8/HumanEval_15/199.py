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
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Outputs: '0'
print(string_sequence(5))  # Outputs: '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `join()` method to concatenate the numbers as strings, separated by spaces. The `range(n + 1)` generates the numbers from 0 to `n`, and the `str(i)` converts each number to a string. The script also includes example use cases to demonstrate the function's behavior.