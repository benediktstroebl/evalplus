### Unique Elements in a List
#### Problem Statement
Return sorted unique elements in a list.

#### Solution
```python
def unique(l: list) -> list:
    """
    Return sorted unique elements in a list.
    
    Args:
    l (list): The input list.
    
    Returns:
    list: A list of sorted unique elements.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list `l` as input, converts it to a set to remove duplicates, and then sorts the resulting set before returning it. The `sorted` function is used to sort the elements in ascending order.