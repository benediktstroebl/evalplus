```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, converts it to a set (which automatically removes duplicates), and then sorts the resulting set. The `sorted` function is used with no arguments other than the set, so it will sort in ascending order by default. 

The `# Example usage:` line shows how to use the function with the provided example input.