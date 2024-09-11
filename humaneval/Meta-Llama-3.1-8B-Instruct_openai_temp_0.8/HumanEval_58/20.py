### Common Elements in Two Lists

Here's a Python function that finds the common elements in two lists, eliminates duplicates, and sorts the result.

```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
    l1 (list): The first list.
    l2 (list): The second list.

    Returns:
    list: A sorted list of unique common elements.

    Example:
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    return sorted(set(l1) & set(l2))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

In this code:

1.  We define a function `common(l1, l2)` that takes two lists `l1` and `l2` as input.
2.  Inside the function, we use the `set` data structure to eliminate duplicates from both lists.
3.  We use the `&` operator to find the intersection of the two sets, which contains the common elements.
4.  We convert the intersection back to a list and sort it using the `sorted` function.
5.  Finally, we return the sorted list of unique common elements.

This solution is concise, readable, and efficient, as it leverages the built-in capabilities of Python's `set` and `sorted` functions.