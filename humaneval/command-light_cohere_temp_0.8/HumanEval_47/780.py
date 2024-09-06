```python
def median(l: list):
    """Return median of elements in the list l"""
    m = float('inf')
    m1 = 0
    for i in range(0, len(l)):
        if l[i] <= m:
            m = l[i]
            m1 = i
    m1 += 1
    if m1 % 2 == 1:
        return (m + l[m1//2]) / 2
    else:
        return m
```