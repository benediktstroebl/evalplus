```python
def median(l: list):
    """Return median of elements in the list l.
    return float(''.split(str(sorted(l)),[1,2])[1])
    """
    return median([i for i in l if i>=0])

def test():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0, " incorrect result "
    return True
```