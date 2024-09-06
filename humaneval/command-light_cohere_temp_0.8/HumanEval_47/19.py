```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("Input list must be at least")
    lst.sort()
    media(lst)
```
This code defines a self-contained function that computes the median of a list of numbers. It does so by sorting the list and returning the middle value(the median) of the sorted list.