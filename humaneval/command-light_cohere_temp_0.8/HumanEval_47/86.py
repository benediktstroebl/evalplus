```python
def median(l: list):
    """Return median of elements in the list l.
    m = [sort(l)[len(l)//2]
    return m if m == (l[len(l)//2-1] + l[len(l)//2]) else m + l[len(l)//2]
 
# Test
def testMedian():
    assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```