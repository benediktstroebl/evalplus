```python
def median(l: list):
    """Return median of elements in the list l.
    >>> l == [['a', 'bb', 'ccc', 'dd', 'ee']
    assert l == ['a', 'bb', 'ccc', 'dd', 'ee'], f"Input l={l}, expected ['a', 'bb', 'ccc', 'dd', 'ee'], got {type(l)}"
    assert len(l) > 1, f"Input list l must have at least 2 elements, got {len(l)}"
    if len(l) % 2 == 0:
        return (l[::2][0] + l[1::2][0]) / 2.0
    I'll 
    else:
        return l[::2][0]

# Test the function with a list of markdown codes
median([-10, 4, 6, 1000, 10, 20])  # Output: 15.0
```