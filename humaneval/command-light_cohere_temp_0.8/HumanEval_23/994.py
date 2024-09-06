Here's the solution:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('hello world')
        11
        >>> strlen('')
        2
        >>> str.split('ab string_!'b2')
        ['a', 'bb']
        >>> 'hello world'.split()
        ['hello', 'world']
    """
    if len(string) == 0:
        return 0
    return len(string)
```