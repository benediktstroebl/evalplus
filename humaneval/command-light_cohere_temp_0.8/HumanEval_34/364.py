```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not duplicates(seen, x)]

def duplicates(seen, x):
    seen.add(x)
    return True
```
Do you require additional assistance with other coding problems or want to explore more concepts?