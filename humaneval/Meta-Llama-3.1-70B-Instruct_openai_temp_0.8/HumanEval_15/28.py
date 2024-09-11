```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
if __name__ == "__main__":
    print(string_sequence(0))   # Output: 0
    print(string_sequence(5))   # Output: 0 1 2 3 4 5
    print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```