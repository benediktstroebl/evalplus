```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    
    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.
    
    Returns:
        list: A sorted list of unique elements that are present in both input lists.
    
    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list

# Test the function with some example inputs
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists `l1` and `l2` as input and returns a sorted list of unique elements that are present in both input lists. It uses Python's built-in `set` data structure to efficiently find the common elements and then converts the result back to a list and sorts it before returning it. The script also includes some example usage of the `common` function to demonstrate its behavior.