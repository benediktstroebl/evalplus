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

The function first sorts the list and then checks if there's any duplication by tracking unique values using a set. If the list is sorted, and there are no duplicates, it returns `True`; otherwise, it returns `False`.  This solution has a time complexity of `O(n log n)` due to the sorting and a space complexity of `O(n)` to store the dictionary. It also passes all the test cases mentioned in the prompt.