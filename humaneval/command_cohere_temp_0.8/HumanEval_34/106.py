```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements. The function first removes any duplicate elements using the `set()` function and then sorts the unique elements using the `sort()` method. 

Let's consider an example where we have a list of numbers [5, 3, 5, 2, 3, 3, 9, 0, 123]. The unique function sorted and removed duplicates, and the result would be [0, 2, 3, 5, 9, 123]. 

This code segment adheres to Python's style standards, specifically for docstrings and type hints, providing a clear understanding of the function's purpose and expected input.