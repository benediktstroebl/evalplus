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

    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, finds the common elements by converting them to sets and finding their intersection, removes duplicates, sorts the result, and returns it. The example usage is shown at the end. 

This solution has a time complexity of O(n + m), where n and m are the lengths of the input lists. This is because we are converting the lists to sets, which takes O(n + m) time, and then finding the intersection of the two sets, which also takes O(n + m) time. The sorting operation at the end has a time complexity of O(k log k), where k is the number of common elements. However, since k is typically much smaller than n + m, the overall time complexity remains O(n + m).