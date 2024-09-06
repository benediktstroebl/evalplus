```python
def median(l):
    """Return median of elements in the list l.
    assert len(l)==len(set(l))
    assert all(x>0 for x in l)
    if len(l)==1:
        return l[0]
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]
    return (len(left)+len(right))/round(len(l)/2)
```