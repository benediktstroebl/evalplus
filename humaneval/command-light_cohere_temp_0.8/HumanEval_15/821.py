Here is a self-contained Python script with a function that solves the problem of generating a string of space-separated numbers:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-separated numbers starting from 0 up to n.
    >>> s = string_sequence(0)
    '0'
    >>> s = string_sequence(5)
    '0 1 2 3 4 5'
    """
    s = ['0']
    while len(s) < n:
        s.append(str(len + 1))
    return ' '.join(s)
```