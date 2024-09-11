### Common Elements in Two Lists
#### Problem Description
Find the sorted unique common elements in two lists.

#### Solution

```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))

    return common_list

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements. It uses Python's built-in set data structure to efficiently find the common elements and then converts the result back to a list and sorts it. The example usage at the end demonstrates how to use the function with different input lists.