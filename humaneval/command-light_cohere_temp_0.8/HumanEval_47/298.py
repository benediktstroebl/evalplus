```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==len(sorted(l))
    assert all(x>0 for x in l)
    if len(l)==2:
        return (l[0]+l[1])/2
    else:
        return l[len(l)-1]
# Example usage
median([-10, 4, 6, 1000, 10, 20])
```