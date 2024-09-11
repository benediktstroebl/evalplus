```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

In this script, we define the `unique` function, which takes a list as input and returns a new list containing the unique elements in the input list, sorted in ascending order. The `set` function is used to remove duplicates, and the `sorted` function is used to sort the resulting set into a list.