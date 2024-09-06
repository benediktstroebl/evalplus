```python
def median(lst):
    """Return the median of elements in the list lst.
    if len(lst) <= 1:
        return lst[0]
    m = []
    for i in range(len(lst)//2):
        m.append(lst[i])
    m.append(lst[(i+1)])
    return sum(m)/len(m) if len(m)==2 else m[0]

# Test suite
for i in range(10):
    print(median([-10, -4, -6, i, -10, -20]))
```