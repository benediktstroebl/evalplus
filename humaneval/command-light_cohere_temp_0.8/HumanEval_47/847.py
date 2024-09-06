```python
def median(l: list):
    """Return median of elements in the list l."""
    if len(l) <= 1:
        return l[0]
    m = l[len(l)//2]
    i = len(l)//2
    while i >= 1 and l[i-1] > m:
        i -= 1
    return m
```