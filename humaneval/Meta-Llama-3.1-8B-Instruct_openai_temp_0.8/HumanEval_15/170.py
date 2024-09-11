### Self-Contained Python Script
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The number up to which the sequence is generated.

    Returns:
        str: A string of space-delimited numbers.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
This script defines the `string_sequence` function, which uses a generator expression to generate the numbers from 0 up to `n` (inclusive) and joins them into a string with spaces in between. The function is then tested with two example calls.