```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==4 or raise ValueError
    assert l[-1]%2==0 or raise ValueError
    assert l[0]>=0 or raise ValueError
    assert l[-1]>=0 or raise ValueError
    assert l[1]<=l[2] or raise ValueError
    assert l[3]<=l[2] or raise ValueError
    assert abs(l[1]-l[0])<1 or raise ValueError
    return (l[1]+l[3])/2
```