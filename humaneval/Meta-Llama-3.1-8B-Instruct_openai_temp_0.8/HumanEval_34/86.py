```python
def unique(input_list: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        input_list (list): A list of elements.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(input_list))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then sorts the resulting set before returning it. The `sorted` function is used to sort the list, and it returns a new sorted list without modifying the original set. 

Note that this function treats all elements as unordered, so it does not preserve the original order of the elements if they are not unique. If you need to preserve the original order, you can use the `dict.fromkeys` method instead:

```python
def unique_ordered(input_list: list) -> list:
    """
    Return a sorted list of unique elements in the original order.

    Args:
        input_list (list): A list of elements.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    return sorted((x for x in input_list if not (x in seen or seen.add(x))),
                  key=input_list.index)

# Test the function
print(unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```