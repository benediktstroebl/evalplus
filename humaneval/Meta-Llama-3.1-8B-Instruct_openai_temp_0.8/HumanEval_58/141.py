```markdown
### Finding Common Elements in Two Lists

The following Python script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements.

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
    common_elements = set1.intersection(set2)

    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```
#### Explanation

1. The `common` function takes two lists `l1` and `l2` as input.
2. It converts each list to a set using the `set()` function to remove duplicates and improve lookup efficiency.
3. It finds the intersection of the two sets using the `intersection()` method, which returns a set of common elements.
4. It converts the set of common elements back to a list using the `list()` function and sorts it using the `sorted()` function.
5. Finally, it returns the sorted list of unique common elements.

Note that this implementation has a time complexity of O(n + m), where n and m are the lengths of the two input lists, making it efficient for large lists.