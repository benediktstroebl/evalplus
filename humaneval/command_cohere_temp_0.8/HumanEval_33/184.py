```python
def sort_third(l):
    return l[:] [[x, min(x, y) if i%3 else max(x, y) ] for i, (x, y) in enumerate(zip(l, sorted(l)[:-1])) if i%3 == 0]
```