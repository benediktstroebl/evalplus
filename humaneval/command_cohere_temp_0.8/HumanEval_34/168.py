```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This approach uses a set, `seen`, to keep track of unique elements encountered while iterating over the input list `l`. Elements that are not already in the set are added to the result list, which ensures only unique elements are included. Finally, the result list is sorted to provide a consistent order of unique elements. 

This code is efficient, with a time complexity of O(n log n) due to the sorting step, where n is the number of elements in the input list. It also has an efficient space complexity of O(n) due to the incremental memory usage by the set and result list.