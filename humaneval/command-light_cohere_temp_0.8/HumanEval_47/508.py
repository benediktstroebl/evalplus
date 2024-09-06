```python
def median(l: list):
    """Return median of elements in the list l."""
    m = []
    for x in l:
        m.append(x)
    m.sort()
     # m is sorted in ascending order
    median = (m[len(m)//2] + m[(len(m)-1)//2])/2
    return median
```