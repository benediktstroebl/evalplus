```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, float('inf')] and seen.add(x)]
```

The function `unique` takes a list as an argument and returns a new list containing only the unique elements in the original list. It uses a
set to keep track of seen elements and creates a new list containing only the elements not previously encountered in the list. This method efficiently solves the