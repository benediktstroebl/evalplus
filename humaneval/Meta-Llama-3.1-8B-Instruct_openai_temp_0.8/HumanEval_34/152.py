```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert list to a set to remove duplicates, then convert back to list
    # and sort it
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines the function `unique` that takes a list as input, removes duplicates by converting it to a set, and then returns the sorted list of unique elements. The test at the end calls the function with the provided example list and prints the result.