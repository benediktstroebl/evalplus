Here's a self-contained Python function that computes and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    undesrieriable: Input string is not a non-empty string
    """
    if not string:
        raise ValueError("Input string is not a non-empty string")

    return len(string)
```