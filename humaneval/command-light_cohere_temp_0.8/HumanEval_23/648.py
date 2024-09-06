Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<string>", line 6, in strlen
        AssertionError:AssertionError: UnboundLocalVariable: 'string' not assigned before instantiation of strlen()
    )
    """
    return len(string)
```