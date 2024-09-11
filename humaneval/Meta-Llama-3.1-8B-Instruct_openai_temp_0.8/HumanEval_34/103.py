### Unique Elements in a List
#### Problem: Return sorted unique elements in a list

```python
def unique_elements(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        lst (list): Input list containing elements to be made unique.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique_elements([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(lst)
    
    # Convert the set back to a list and sort it
    sorted_unique_list = sorted(list(unique_set))
    
    return sorted_unique_list

# Example usage:
print(unique_elements([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique_elements` that takes a list as input, removes duplicates by converting it to a set, and then converts it back to a list and sorts it. The sorted list of unique elements is then returned. The example usage at the end demonstrates how to use this function.