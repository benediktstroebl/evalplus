```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage
print(string_sequence(0))  # Outputs: 0
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```