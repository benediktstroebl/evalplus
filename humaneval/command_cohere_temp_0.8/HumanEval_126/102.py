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

The function first sorts the list and then checks if there's any duplication by tracking unique values using a set. If there's any duplicate in the list, it will return `False`. Otherwise, it will return `True`. 

This approach has a time complexity of O(n log n) due to the sorting step and O(n) for the check of duplicates. It uses the built-in `sort()` function for sorting, which works well for all integers and is generally efficient for the given problem.