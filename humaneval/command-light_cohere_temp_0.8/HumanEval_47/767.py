```python
def median(l):
    """Return median of elements in the list l."""
    m = []
    for x in l:
        m.append(x[m:int(len(m)/2), x])
    return (sum(m)/float(len(m))))
# Test cases
assertEqual(median([3, 1, 2, 4, 5]), 3)
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 10)
assertEqual(median([1, 2, 3, 4, 5, 6]) , 4.5)
```