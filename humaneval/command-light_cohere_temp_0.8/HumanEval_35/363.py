```python
def max_element(l: list):
    """Return maximum element in the list
    >>> l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    >>> max_element(l)
    123
    >>> l.append(1)
    l.append(-20)
    maximum element is a number: 7
    >>> max_element([1, 2, 3, 4, 5])
    5
    """
    return max(l)
```