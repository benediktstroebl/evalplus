```python
def median(l: list):
    """Return median of elements in the list l.
    return float('median'([ele for ele in l if ele not float]))
    """
    l = [ele for ele in l if ele not float]
    return float(sorted(l)[len(l)//2])
```