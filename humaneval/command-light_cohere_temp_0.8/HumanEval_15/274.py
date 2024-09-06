```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 up to n.
    >>> string_sequence(0) == '0'
    >>> string_sequence(1) == '1'
    >>> string_sequence(5) == '0 1 2 3 4 5'
    >>> string_sequence(6) == '0 1 2 3 4 5 6'
    """
    return ''.join(str(i) for i in range(n))
```