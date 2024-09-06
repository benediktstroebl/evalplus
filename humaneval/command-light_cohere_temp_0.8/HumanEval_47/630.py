```python
def median(l):
    """Return median of elements in the list l."""
    m = []
    for x in l:
        m.append(x) if m and (len(m)) // 2 else m.pop(0)
    m.median(sorted(m))
    return float(m[-1])
# Test cases
# Test 1
med = median([-10, 4, 6, 1000, 10, 20])
print('Median of [-10, ..., 1000] is:', med)

# Test 2
l = [2, 4, -10, 6, -20, -30]
med = median(l)
print('Median of [2, 4, ..., -30] is:', med)

# Test 3
l = [1, 2, 3, 4, 5]
med = median(l)
print('Median of [1, ..., 5] is:', med)
```