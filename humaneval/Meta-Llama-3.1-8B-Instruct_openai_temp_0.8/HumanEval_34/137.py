```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    
    Args:
        lst (list): The input list.
    
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

In this script, we define a function `unique` that takes a list as input, converts it to a set (which removes duplicates), and then sorts the resulting set. The sorted list of unique elements is then returned.

Note: This solution has a time complexity of O(n log n) due to the sorting step, where n is the number of elements in the list. If you need a more efficient solution that preserves the original order of elements, you can use a different approach, such as using a dictionary to keep track of unique elements or using a `collections.OrderedDict` with a custom key function.