```python
def is_sorted(lst):
    lst.sort()   
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list and then checks if there's any duplication by tracking unique values using a set. If there's any duplication, it returns false immediately. If no duplication is detected, it returns true.