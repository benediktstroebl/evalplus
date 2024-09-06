```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The function unique takes a list l as input and returns a list of unique elements from l, sorted in ascending order. The function uses a set seen to track elements already encountered, initialized with no elements. The list comprehension iterates over each element x in l if either (1) x is not in seen (i.e., not encountered before) or (2) seen.add(x) is invoked to add x to seen, appending x to result. Finally, the function returns sorted(result), sorting result in ascending order.

This solution is relatively efficient with a time complexity of O(n log n) due to the sorting and set operations.

This code block solves the given problem and should be executable directly in a Python environment.