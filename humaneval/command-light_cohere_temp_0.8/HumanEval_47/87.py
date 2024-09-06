```python
def median(l: list):
    """Return median of elements in the list l.
    n = len(l)
    if n < 1:
        return None
    
    mid = n // 2
    i = j = 0
    while i < mid:
        if l[i] > l[j]:
            j = i
        i += 1
    
    while j < n - 1:
        if l[j] > l[j + 1]:
            j += 1    
    m = l[j]
    j += 1
    while j < n:
        if l[j] == m:
            j += 1
        else:
            break
    return m
```