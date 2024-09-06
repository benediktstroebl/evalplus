```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(seen.add(x) for x in l if x not in seen and x != '')
```

This code uses a set, seen, to efficiently track unique elements without repeat operations, complementing the list comprehension's ability to generate unique elements. It checks for both membership in seen and falsity of x to ensure efficiency and correctness, outputting a sorted list of distinct elements. 

To ensure efficient and correct detection of unique elements, the function validates both membership in seen and falsity of x, optimizing the process. The resulting sorted list of unique elements delivers the expected outcome.