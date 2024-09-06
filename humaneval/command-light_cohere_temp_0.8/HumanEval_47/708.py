```python
def median(l: list):
    """Return median of elements in the list l."""
    if len(l) <= 1:
        return l[0]
    mid = len(l) // 2
    if l[mid] > l[-1-mid]:
        return (l[mid] + l[-1-mid]) / 2
    return l[mid]
```
The function median takes a list as input and returns the median value of the elements in that list. It does this by finding the median of the two middle elements of the sorted list, and then taking the average of those two values.