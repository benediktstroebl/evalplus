### Common Elements in Two Lists
#### Code
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
    # Convert lists to sets to remove duplicates and optimize lookup
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

#### Explanation

This script defines a function `common` that takes two lists `l1` and `l2` as input. It converts these lists to sets to remove duplicates and optimize lookup. Then it finds the intersection of the two sets using the `&` operator, which returns a set of common elements. Finally, it converts this set back to a list, sorts it, and returns the result.

The script includes documentation comments to explain what the function does, its input and output parameters, and provides example usage to demonstrate its functionality.