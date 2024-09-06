```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements present in `l`. The algorithm first removes duplicate elements using the `set()` function and then sorts the unique elements by passing the resulting set to the `sort()` function. 

This solution effectively and efficiently addresses the problem statement by providing the functionality to obtain sorted unique elements from a given list.

The implementation adheres to Python's coding standards and the function is suitably annotated with a docstring to describe its purpose and behavior, making it easily understandable by other developers.