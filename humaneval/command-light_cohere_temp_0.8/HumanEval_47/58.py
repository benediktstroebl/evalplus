```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("List is empty.
    m = l[0] + (l[-1] + l[-2]) / 2
    return m
    ```