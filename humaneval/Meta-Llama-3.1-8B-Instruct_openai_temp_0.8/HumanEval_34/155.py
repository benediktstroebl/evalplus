### Unique Elements in a List
#### Problem Description
This script returns a sorted list of unique elements from the input list.

#### Code
```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list

    Args:
        lst (list): The input list

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

#### Explanation
The `unique` function uses the built-in `set` function to remove duplicates and then sorts the resulting list using the `sorted` function. The `set` function converts the list into a set, which automatically removes duplicates, and then the `sorted` function sorts the set in ascending order.