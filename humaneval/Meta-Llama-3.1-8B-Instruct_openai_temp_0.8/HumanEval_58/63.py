```markdown
### Common Elements in Two Lists
#### Problem Description
This script takes two lists as input and returns a new sorted list containing unique elements that are common to both input lists.

#### Code
```python
def common(l1: list, l2: list) -> list:
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
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., common elements)
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    result = sorted(list(common_elements))

    return result
```

#### Example Usage
```python
# Test the function with the provided examples
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```
This script uses Python's built-in `set` data structure to efficiently find common elements between the two input lists. The `&` operator is used to compute the intersection of the two sets, which results in a new set containing only the common elements. Finally, the script converts this set back to a list, sorts it, and returns the result.