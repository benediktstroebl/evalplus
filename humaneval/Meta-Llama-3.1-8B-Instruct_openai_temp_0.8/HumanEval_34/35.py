```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function called `unique` that takes a list as input, removes duplicates by converting it to a set, and then returns the sorted list of unique elements. The `sorted` function is used to sort the set in ascending order, which is the default sorting order. 

The example usage demonstrates how to use the `unique` function by printing the sorted list of unique elements for the given list.