```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    
    Args:
        lst: A list of elements
    
    Returns:
        A sorted list of unique elements
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we define a function `unique` that takes a list `lst` as input. It returns a sorted list of unique elements using the following steps:

1. Convert the original list to a set to remove duplicates.
2. Convert the set back to a list.
3. Sort the list.

The `sorted` function is used to sort the list in ascending order. The `set` function is used to remove duplicates from the list.

The script includes a test case at the end to demonstrate the usage of the `unique` function. When you run this script, it will print the sorted list of unique elements `[0, 2, 3, 5, 9, 123]`.