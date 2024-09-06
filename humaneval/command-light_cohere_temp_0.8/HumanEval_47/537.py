```python
def median(l):
    """Return median of elements in the list l"""
    return (sorted((e for e in l), reverse=True)[:len(l) // 2])[0]
```
This function sorts the list and then returns the middle element (or the average of the two middle elements, if the length is odd), as the median.