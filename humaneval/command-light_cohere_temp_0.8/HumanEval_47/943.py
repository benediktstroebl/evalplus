```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==len(set(l)), 'List must be unique'
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        m1 = median(l[::2])
        m2 = median(l[-2::-2])
        return (m1+m2)/2
```