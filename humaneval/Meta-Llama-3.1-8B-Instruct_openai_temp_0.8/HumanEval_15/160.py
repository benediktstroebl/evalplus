```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))


# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence(n)` that generates a string sequence from 0 to `n` inclusive. The function uses the built-in `join()` method to concatenate the numbers into a space-delimited string. The numbers are generated using a generator expression within the `range(n + 1)` function. The `+ 1` is used to include `n` in the sequence. The test cases at the end demonstrate the function's behavior with different inputs.