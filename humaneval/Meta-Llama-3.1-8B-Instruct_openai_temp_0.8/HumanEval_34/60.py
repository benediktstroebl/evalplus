```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
    lst (list): The list to find unique elements in.

    Returns:
    list: A sorted list of unique elements.

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:
- We use the built-in `set` function to remove duplicates from the list, because sets in Python cannot contain duplicate elements.
- The `set` function returns a set, which is an unordered collection of unique elements. Since the problem requires the elements to be in sorted order, we use the `sorted` function to convert the set back into a sorted list.
- The `sorted` function returns a new sorted list and leaves the original list unaffected.