```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): A list of elements

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function called `unique` that takes a list `l` as an argument. It uses the `set` function to remove duplicates from the list, and then uses the `sorted` function to sort the remaining elements in ascending order. The sorted list of unique elements is then returned.

When you run this script, it will print the sorted list of unique elements from the example list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`, which is `[0, 2, 3, 5, 9, 123]`.