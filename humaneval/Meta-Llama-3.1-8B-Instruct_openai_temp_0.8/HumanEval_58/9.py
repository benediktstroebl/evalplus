### Common Elements in Two Lists

The following Python script defines a function `common` that returns the sorted unique common elements from two input lists.

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
    # Convert lists to sets for efficient operations
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list, sort it, and return it
    return sorted(list(common_elements))

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script works by first converting the input lists to sets, which allows for efficient set operations like intersection (`&`). The intersection of two sets contains all elements that are present in both sets, which are the common elements in the two lists. The script then converts the set back to a list, sorts it, and returns it.