```markdown
## common.py
### Returns sorted unique common elements for two lists

```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A list of sorted unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]

    """
    return sorted(set(l1) & set(l2))
```

### Example usage:
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```
This script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements. The function uses Python's set intersection operator `&` to find the common elements, which are then converted to a sorted list using the `sorted` function. The example usage demonstrates how to call the `common` function with different inputs.
```