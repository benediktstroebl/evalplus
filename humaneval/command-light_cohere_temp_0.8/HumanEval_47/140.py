```python
def median(l):
    """Return median of elements in the list l.
    l = [list([-10, 4, 6, 1000, 10, 20])
    m = (sorted(l) if len(l)>1 else [l[0]])
    return float(m[len(m)//2])
# Test the function
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```