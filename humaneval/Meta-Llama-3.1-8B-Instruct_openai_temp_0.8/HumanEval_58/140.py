```markdown
## Common Elements in Two Lists

This script defines a function `common` that finds and returns the sorted unique common elements in two input lists.

### Code

```python
def common(l1: list, l2: list) -> list:
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
    s1 = set(l1)
    s2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = s1 & s2

    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))

    return result
```

### Example Usage

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
```
```

This script defines a function `common` that takes two lists as input, finds their intersection using set intersection operation, removes duplicates, and returns the sorted result. The example usage demonstrates the function's behavior with the provided test cases.