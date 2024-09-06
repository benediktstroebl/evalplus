```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2 * (sorted((l + [0]))[1] or float('inf'))
```
This function computes the median of a list by using the length of the list and the list itself, which avoids external dependencies and provides a self-contained solution for the median calculation.