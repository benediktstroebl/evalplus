### Common Elements in Two Lists
#### Problem Statement
Find the sorted unique common elements in two lists.

#### Solution
```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: The sorted unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```
#### Explanation
This script defines a function `common` that takes two lists as input and returns the sorted unique common elements. It uses sets to remove duplicates and improve lookup efficiency. The function first converts the input lists to sets, finds the intersection of the two sets, converts the result back to a list, and sorts it before returning it. The script includes test cases to demonstrate the function's correctness.