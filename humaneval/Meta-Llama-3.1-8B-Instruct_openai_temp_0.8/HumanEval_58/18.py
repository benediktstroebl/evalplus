Here's a Python script that solves the problem:
```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.
    
    Args:
    l1 (list): The first list.
    l2 (list): The second list.
    
    Returns:
    list: A sorted list of unique common elements.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements


# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```
This script uses Python's built-in set data structure to efficiently find the common elements between two lists. Sets automatically remove duplicates and have fast lookup times, making them ideal for this problem. The `&` operator is used to find the intersection of the two sets, and the result is converted back to a list and sorted before being returned.