### Common Elements in Two Lists

Below is a Python script that defines a function to find and return the sorted unique common elements in two lists.

```markdown
### Code
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
    # Find the intersection of two lists using set intersection operation
    common_elements = set(l1).intersection(set(l2))
    
    # Convert the set back to a list, sort it, and return
    return sorted(list(common_elements))


# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

### Explanation

1. The function `common(l1, l2)` takes two lists as input and returns a sorted list of unique common elements.
2. The `set()` function is used to convert the lists to sets, which automatically removes duplicates.
3. The `intersection()` method is used to find the common elements in both sets.
4. The `sorted()` function is used to sort the common elements in ascending order, and `list()` is used to convert the set back to a list.
5. The function includes docstrings for clarity and example use cases.
6. The script includes test cases to demonstrate the function's usage.