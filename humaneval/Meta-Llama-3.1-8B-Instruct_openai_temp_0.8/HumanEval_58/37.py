### Finding Common Elements in Two Lists
#### Problem Description
Given two lists, `l1` and `l2`, this script finds and returns the sorted unique common elements between the two lists.

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
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set_l1 = set(l1)
    set_l2 = set(l2)
    
    # Find common elements
    common_elements = set_l1 & set_l2
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

#### Explanation
This script uses Python's built-in `set` data structure to find the common elements between two lists. Here's a step-by-step breakdown of how it works:

1. Convert the input lists to sets using the `set()` function. This removes any duplicate elements and provides an efficient way to find common elements.
2. Use the `&` operator to find the intersection of the two sets, which gives us the common elements.
3. Convert the resulting set back to a list using the `list()` function and sort it using the `sorted()` function.
4. Return the sorted list of common elements.

This approach has a time complexity of O(n + m), where n and m are the lengths of the input lists, making it efficient for large inputs.