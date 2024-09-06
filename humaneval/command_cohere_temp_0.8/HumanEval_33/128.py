```python
def sort_third(l):
    return l[:] [[x, sorted(y) if i==0 else y[i:] + [y[i-1]]] for i, x in enumerate(l) for y in [x]]
```