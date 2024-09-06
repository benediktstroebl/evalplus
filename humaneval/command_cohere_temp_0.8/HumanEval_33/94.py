```python
def sort_third(l):
    return l[:] if not l or len(l) % 3 else sorted([x for i, x in enumerate(l) if i % 3 == 0]) + l[len(l) // 3:len(l) // 3 * 2] + sorted([x for i, x in enumerate(l[len(l) // 3:len(l) // 3 * 2]) if i % 3 != 0])
```