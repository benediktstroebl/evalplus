```python
def sort_third(l):
    return l[:] [[x, sorted(y) if i%3 else y for x,y in zip(l,l)] for i in range(len(l))]
```