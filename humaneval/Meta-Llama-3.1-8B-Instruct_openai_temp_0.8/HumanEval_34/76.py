### Unique Elements in a List

Here's a simple Python script that uses a set to remove duplicates and a sorted list to maintain the sorted order.

```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list

    Args:
        lst (list): The list to remove duplicates from.

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

In this script:

*   We define a function `unique` that takes a list `lst` as input and returns a sorted list of unique elements.
*   Inside the function, we use `set` to remove duplicates because sets in Python cannot contain duplicate values.
*   We then use `sorted` to sort the unique elements in ascending order.
*   We provide an example usage of the function to demonstrate its behavior.

This script is concise, readable, and well-documented, making it easy to understand and use.