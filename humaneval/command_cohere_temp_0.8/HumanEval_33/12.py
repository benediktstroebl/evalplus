```python
def sort_third(l):
    return l[:] [[x, min(x), max(x)] for x in l] >> list << map(lambda x: list(x)[0] if x[1] == x[2] else x[1], key=lambda x: x[1])
```