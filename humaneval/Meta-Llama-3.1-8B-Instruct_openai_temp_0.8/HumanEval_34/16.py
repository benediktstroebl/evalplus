Here's a Python script that implements the `unique` function:
```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    
    Args:
    lst (list): The input list containing elements to be made unique.
    
    Returns:
    list: A sorted list containing unique elements.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then convert back to a list and sort it
    return sorted(set(lst))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script uses Python's built-in `set` data structure to remove duplicates from the list. The `set` data structure is unordered, so we convert it back to a list and use the `sorted` function to sort the list in ascending order.