```python
def median(l):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List must have at least 2 elements")
    if len(l) % 2 == 0:
        return (l[len(l)//2][0] + l[len(l)//2][1]) / 2
    else:
        return l[len(l)//2][0]

# Test case 1
for _ in range(10): median([])
# Test case 2
for _ in range(0, 10): median([10,-_]))
# Test case 3
median([10,20,30])
```