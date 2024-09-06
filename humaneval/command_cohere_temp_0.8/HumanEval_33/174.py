```python
def sort_third(l):
    return l[:] [[x, min(y for y in l if y % 3 == 0 and y > x), max(y for y in l if y % 3 == 0 and y < x)] for x in l if x % 3 != 0]]
```