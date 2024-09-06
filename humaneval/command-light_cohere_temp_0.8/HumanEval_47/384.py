```python
def median(l: list):
    """Return median of elements in the list l."""
    return (getMedian(l, 2) + getMedian(l, 1)) / 2.0

def getMedian(l: list, k: int):
    """Return kth median of the list l."""
    if k == 0:
        return float('inf')
    if k == 1:
        return l[0]
    m = [x for x in l if k == (len(l) - 1) // 2]
    return getMedian(m, k - 1)
```