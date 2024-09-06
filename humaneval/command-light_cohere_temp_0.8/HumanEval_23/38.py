```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    File "<filename>", line 1, in <module>:\
    strlen()
    File "<stdin>", line 5, in <main>
    File "<stdin>", line 4, in '...'
    File "<stdin>", line 2, in <string>
    ValueError: unimplemented operand type
    """
    if not string:
        return 0
    try:
        return len(string)
    except ValueError:
        print("Error: Unimplemented operand type")
```