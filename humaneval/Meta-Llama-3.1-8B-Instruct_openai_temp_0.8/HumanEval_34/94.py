```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Use a set to remove duplicates, then convert back to a list and sort
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we define a function `unique` that takes a list as input. We use a set to remove duplicate elements (sets in Python are unordered collections of unique elements), then convert this set back to a list and sort it using the `sorted` function. The result is a sorted list of unique elements from the input list.