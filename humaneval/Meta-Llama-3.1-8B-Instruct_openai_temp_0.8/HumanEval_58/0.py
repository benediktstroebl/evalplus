```python
def common(l1: list, l2: list):
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
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., common elements)
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    sorted_common_elements = sorted(list(common_elements))

    return sorted_common_elements

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
```

In this script, we define a function `common` that takes two lists as input and returns a sorted list of unique common elements. The function uses Python's built-in set data structure to improve lookup efficiency and remove duplicates. The set intersection operation (`&` operator) is used to find the common elements, which are then converted back to a list and sorted before being returned. The example usage at the end of the script demonstrates how to call the `common` function with different input lists.