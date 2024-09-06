```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This approach utilizes a set, `seen`, to keep track of unique elements encountered while iterating through the list `l`. Elements not in the set are added to the result list, which ensures only unique elements are included. Finally, the result list is sorted to provide a consistent order of unique elements.

Here is a more detailed breakdown of the steps:
1. Use a list comprehension to create a new list, `result`, that contains all elements from `l` that are not already present in the `seen` set. The `not (x in seen or seen.add(x))` condition effectively checks if the element `x` is not already in the set `seen` and adds it if it's not.
2. Sort the `result` list using the `sorted()` function to ensure a consistent order of unique elements.
3. Return the sorted result.

This approach is efficient and guarantees both uniqueness and a specific order for the elements.