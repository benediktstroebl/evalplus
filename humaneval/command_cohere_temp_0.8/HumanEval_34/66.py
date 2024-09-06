```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list comprehension to efficiently filter out duplicate elements and ensure uniqueness. The 'not seen.add(element)' expression checks whether an element is about to be added to the set, which is an O(1) operation in a set, and the sorting is handled by the list comprehension. Overall, the solution is both efficient and succinct.