### Common Elements in Two Lists
#### Problem Statement
Return sorted unique common elements for two lists.

#### Solution
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
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```
This script defines a function `common` that takes two lists as input, finds their common elements using set intersection, removes duplicates, and returns the sorted list of common elements. The example usage demonstrates the function's behavior with two different input pairs.