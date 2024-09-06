```python
def max_element(l: list):
    """Return maximum element in the list
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123])
    123
    >>> max_element([])
    0
    >>> max_element([-1000, -100, -5])
    -1000
    >>> max_element([1, 2, 3, 4, 5])
    5
    >>> max_element([]) raise Exception
    """
    if not l:
        return 0
    try:
        return max(l)
    except:
        raise Exception("error")
```