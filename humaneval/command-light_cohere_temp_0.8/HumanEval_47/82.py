```python
def median(l: list):
    """Return median of elements in the list l.
    >>> assert len(l) > 1
    assert median(l[:int(len(l) / 2)]) == median(l[len(l) :])
    return median(l)

median([3, 1, 2, 4, 5]) # Output: 3.0
median([-10, 4, 6, 1000, 10, 20]) # Output: 5.0
```