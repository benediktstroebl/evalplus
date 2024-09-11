### Common Elements in Two Lists
#### Problem Description

Given two lists of integers, return the sorted unique common elements.

#### Solution
```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list of integers.
        l2 (list): The second list of integers.

    Returns:
        list: Sorted unique common elements.

    Example:
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

    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))

    return result
```
#### Example Usage
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
```
This script uses Python's built-in `set` data structure to efficiently find the common elements between the two lists. The `&` operator is used to compute the intersection of the two sets, and the `sorted` function is used to sort the common elements in ascending order.