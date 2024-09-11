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

In this script, the `unique` function takes a list `l` as input. It uses the `set` function to create a set from the list, which automatically removes duplicates. The `sorted` function is then used to sort the unique elements in ascending order. The result is a sorted list of unique elements from the original list.