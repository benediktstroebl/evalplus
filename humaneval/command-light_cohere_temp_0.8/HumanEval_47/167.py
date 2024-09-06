```python
def median(l):
    # Sort the list in ascending order
    l.sort()
    median = int((len(l) + 1) / 2)
    return l[median]
```