```python
def median(l):
    """Return median of elements in the list l.
    assert(len(l)==5 or len(l) > 0), "Input list must be a list of at least five elements"
    if len(l)==5:
        return (l[3] + l[1]) / 2
    else:
        return l[(len(l) - 1) // 2]

# Test cases
assert(median([3, 1, 2, 4, 5]) == 3.0)
assert(median([-10, 4, 6, 1000, 10, 20]) == 15.0)
```