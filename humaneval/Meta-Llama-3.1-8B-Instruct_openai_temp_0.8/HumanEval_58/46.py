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

    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Use set intersection to find common elements
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements
```
This function first converts the input lists to sets to remove duplicates and improve the efficiency of the lookup operation. It then uses the `&` operator to find the intersection of the two sets, which gives the common elements. Finally, it converts the resulting set back to a list, sorts it, and returns it.

You can use this function as shown in the docstring example.