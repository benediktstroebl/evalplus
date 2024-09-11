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
    s1 = set(l1)
    s2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = s1 & s2
    
    # Convert the set of common elements back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list


# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, finds the common elements by converting them to sets and using the intersection operator `&`, and returns the common elements as a sorted list. The function includes docstrings with examples to provide information about its usage and behavior. The script also includes test cases to verify the correctness of the function.