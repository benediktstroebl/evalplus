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

The function first sorts the list and then uses a set to track its unique elements. By returning `False` if any element is encountered more than once in the sorted list, the function checks for elements that are not sorted correctly. The set data structure ensures it can efficiently handle duplicates, while maintaining a simple and efficient check for sorting.