```python
def sort_third(l):
    return l[:] [[x, sorted(y) if i%3 else y][i%2] for i,x in enumerate(l) for y in [x, l[i]] if i%3]
```