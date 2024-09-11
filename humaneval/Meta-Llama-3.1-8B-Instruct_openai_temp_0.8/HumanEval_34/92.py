```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we use a combination of Python's built-in functions:

- `set()`: removes duplicate elements from a list by converting it to a set, which automatically removes any duplicate values.
- `sorted()`: sorts the list of unique elements in ascending order.

This function is efficient because it has a time complexity of O(n log n) due to the `sorted()` function, where n is the number of elements in the list.