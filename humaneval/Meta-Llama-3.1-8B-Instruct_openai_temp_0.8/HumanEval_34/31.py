```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function takes a list `l` as input, converts it to a set (which removes duplicates) and then converts it back to a list. This list is then sorted in ascending order using the `sorted` function and returned. The example usage demonstrates how to use the function with the provided test case.