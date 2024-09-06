```python
def median(l: list):
    """Return median of elements in the list l"""
    m = 0
    i, j = 0, len(l) // 2
    while i < j:
        if l[i] > l[j]:
            j -= 1
        m += l[i]
        i += 1
    median = m / (j + 1)
    return median
# Suite of tests
for _ in range(0, 5):
    t = [4, -20, 2, 1, 10]
    assert median(t) == 2
```