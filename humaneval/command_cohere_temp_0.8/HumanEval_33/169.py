```python
def sort_third(l):
    return l[:] [[x, min(x), max(x)] for x in l] >> list << map((lambda x: x[0], sorted(x[1:]), x), enumerate(l))
```