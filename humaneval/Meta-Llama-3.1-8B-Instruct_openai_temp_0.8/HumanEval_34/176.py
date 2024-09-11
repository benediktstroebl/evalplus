```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Testing the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:

- The `set()` function is used to remove duplicates from the list.
- The `sorted()` function is then used to sort the resulting set in ascending order.
- This approach has a time complexity of O(n log n) due to the sorting operation.
- It's worth noting that this approach does not preserve the original order of elements. If preserving order is necessary, a different approach would be required, such as using a list comprehension with an if condition to check for uniqueness.