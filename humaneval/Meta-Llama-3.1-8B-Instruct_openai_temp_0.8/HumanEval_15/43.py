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
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function `string_sequence(n)` that generates a string sequence from 0 to `n` (inclusive) and returns it. The function uses a generator expression within the `join()` method to create the string. The `+ 1` in `range(n + 1)` is used to include `n` in the sequence. The script then tests the function with two examples.