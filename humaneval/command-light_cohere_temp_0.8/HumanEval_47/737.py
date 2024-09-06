```python
def median(l: list):
    """Return median of elements in the list l.
    # sort theMate
   
    l = sorted(l)
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
# Test cases
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([3, 1, 2, 4, 5]) == 3
assert median([10, 20, 30, 10, 40]) == 30
assert median([10, 20, 10, 30]) == 10
```