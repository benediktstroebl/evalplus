```python
def unique(lst: list):
    """
    Return sorted unique elements in a list.

    Args:
        lst (list): Input list.

    Returns:
        list: Sorted list with unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script:

*   We define a function `unique(lst)` that takes a list as an input.
*   Inside the function, we use the built-in `set()` function to remove duplicates from the list.
*   We then use the `sorted()` function to sort the unique elements in ascending order.
*   Finally, we return the sorted unique elements.