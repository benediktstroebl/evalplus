```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))


# Testing the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:

1.  The `set()` function is used to create a set from the input list. A set in Python is an unordered collection of unique elements.
2.  The `sorted()` function is then used to sort the set of elements in ascending order.
3.  The `unique()` function is thus a concise way to return sorted unique elements from a list.