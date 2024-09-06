```python
def median(l: list):
    """Return median of elements in the list l.
    assert(is not empty())
    assert(isinstance(l, list)), "Input must be a list."
    assert(all(isinstance(x, (int, float)) for x in l)), "All elements in the list must be numbers."
    assert(l[-1] >= 0), "Last element in the list must be non negative."
    return (l[-1] + l[0]) / 2
```