### Common Elements in Two Lists
#### Problem Description
This script defines a function `common` that takes two lists as input and returns the sorted unique common elements between them.

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
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Example usage:
l1 = [1, 4, 3, 34, 653, 2, 5]
l2 = [5, 7, 1, 5, 9, 653, 121]
print(common(l1, l2))  # Output: [1, 5, 653]

l1 = [5, 3, 2, 8]
l2 = [3, 2]
print(common(l1, l2))  # Output: [2, 3]
```

This script defines the `common` function, which first converts the input lists to sets to remove duplicates and improve lookup efficiency. It then finds the intersection of the two sets using the `&` operator, which returns a new set containing the common elements. The script finally converts this set back to a list, sorts it, and returns the result. The example usage at the end demonstrates how to call the `common` function with two lists and print the result.