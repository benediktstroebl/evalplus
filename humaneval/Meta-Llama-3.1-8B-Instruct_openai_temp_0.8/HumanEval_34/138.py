### Unique Elements in a List
#### Problem Statement
Return sorted unique elements in a list.

#### Solution
```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list

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

In this script, we define a function `unique` that takes a list `l` as input. It uses the `set` function to remove duplicates from the list, and then the `sorted` function to sort the unique elements in ascending order. The result is returned as a list.

When you run this script, it will print the sorted list of unique elements from the example list provided.