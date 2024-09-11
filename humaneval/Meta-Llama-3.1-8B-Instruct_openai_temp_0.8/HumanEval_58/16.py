```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    :param l1: The first list
    :param l2: The second list
    :return: A sorted list of unique common elements
    """
    # Convert lists to sets to remove duplicates and have O(1) lookup time
    set1 = set(l1)
    set2 = set(l2)
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    # Convert the set back to a list and sort it
    return sorted(list(common_elements))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines the `common` function, which takes two lists as input and returns a sorted list of unique common elements. The function uses sets to remove duplicates and have O(1) lookup time, and then converts the result back to a list and sorts it. The script also includes test cases to demonstrate the function's behavior.