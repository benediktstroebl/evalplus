```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we define a function `unique(l: list)` that returns a sorted list of unique elements from the input list `l`. We achieve this by first converting the list to a set, which removes duplicates, and then sorting the resulting set before returning it. The `sorted()` function is used to sort the elements in ascending order.