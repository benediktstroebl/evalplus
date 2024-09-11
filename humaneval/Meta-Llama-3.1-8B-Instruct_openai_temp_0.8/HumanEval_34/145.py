Here's a Python script that uses a set to remove duplicates and then sorts the resulting list:

```python
def unique(l: list):
    """
    Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

The `set()` function removes duplicates from the list because sets in Python cannot contain duplicate elements. However, the set does not preserve the original order of elements, so we use the `sorted()` function to sort the set and return the result.