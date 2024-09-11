```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    :param l: List of elements
    :return: Sorted list of unique elements
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function takes a list `l` as input and returns a sorted list of unique elements. The `set` function is used to remove duplicates, and the `sorted` function is used to sort the resulting set.

The test at the end demonstrates the function's usage by passing a list with duplicate elements and printing the result.