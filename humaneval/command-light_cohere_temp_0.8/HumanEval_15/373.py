Here is a self-contained Python script that defines a function string_sequence that solves the problem of generating a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> string_sequence(10)
    '0 9 8 7 6 5 4 3 2 1'
    >>> string_sequence(13)
    '0 12 11 10 13 14'
    """
    return f'{0}{1} {2}...{n}'
```