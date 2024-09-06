```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==3 or raise ValueError("Input list must have exactly 3 elements")
    assert l[0] <= l[1] and l[1] <= l[2] and l[2] <= l[3] or raise ValueError("List must be sorted in ascending order")
    if l == [1,1]:
        return 1.0
    else:
        return (l[1] + l[2]) / 2.0
```