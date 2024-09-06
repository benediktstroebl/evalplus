```python
def median(l: list):
    """Return median of elements in the list l.
    assert(is is a list of numbers)
    assert(len(l) >= 1)
    assert(all(isinstance(i, (int, float)) for i in l)), 'All elements must be numbers'
    assert(l[0] != float('inf')), 'Last element cannot be infinite'
    assert(l[-1] != float('inf')), 'First element cannot be infinite'

    m = 0
    for i in range(1, len(l)):
        if l[i] > m:
            m = l[i]
    return m
```