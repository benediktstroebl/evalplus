```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 up to n.
    >>> print(string_sequence(0))
    '0'
    >>> print(string_sequence(5))
    '0 1 2 3 4 5'
    >>> print(string_sequence(-1))
    Traceback (most recent call last):
      File "<stdin>", line 8, line 1:
        TypeError: unsupported operand type(1) for + operation: 'string' and int()
    """
    return ''.join(str(x) for x in range(n))
```