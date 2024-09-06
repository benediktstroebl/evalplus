```python
def median(l: list):
    """Return median of elements in the list l.
    assert(len(l) > 1),
    assert(len(l) % 1 == 0), "List should be sorted"
    l.sort()
   med = sorted(l)[len(l) // 2]
    return l[med]
```