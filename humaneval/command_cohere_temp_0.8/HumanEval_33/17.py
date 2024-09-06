```python
def sort_third(l):
    return l[:] [[x, min(x), max(x)] for x in l if x != l[::3][i]][:len(l) // 3]
```