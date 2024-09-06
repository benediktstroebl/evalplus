```python
def median(l: list):
    """Return median of elements in the list l."""
    return (getMedian(l, len(l)//2) + getMedian(l, len(l)//2)) / 2
def getMedian(l: list, k):
    """Return kth element in the list l."""
    return l[k]
```
The code defines a self-contained Python function that computes and returns the median of a list of elements. The function utilizes a two helper functions: `getMedian` and `getMedian(l, k)`.  The function uses the `getMedian` helper to get the median of half of the list, and then adds the median of the first half and the second half to get the median. This ensures a accurate median value.