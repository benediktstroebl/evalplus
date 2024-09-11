```python
def common(l1: list, l2: list):
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

    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1.intersection(set2)

    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines the `common` function, which takes two lists `l1` and `l2` as input, finds their intersection (i.e., the common elements), removes duplicates, and returns the result as a sorted list. The function includes a docstring with a clear description, arguments, and return values. The script also includes two test cases to demonstrate the function's behavior.