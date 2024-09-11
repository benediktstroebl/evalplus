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

Explanation:

1. The `set(l)` function is used to create a collection of unique elements from the input list.
2. The `sorted()` function is then used to sort the unique elements in ascending order.
3. The result is returned by the `unique()` function.

This solution has a time complexity of O(n log n) due to the use of the `sorted()` function, where n is the number of elements in the input list.