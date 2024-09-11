Here's a Python script that defines the `common` function to return sorted unique common elements for two lists:
```markdown
# common_elements.py

def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: The sorted unique common elements.

    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Use set intersection to find the common elements
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```
This script defines the `common` function to take two lists as input, convert them to sets to remove duplicates and improve lookup efficiency, find the common elements using set intersection, convert the result back to a list, sort it, and return it. The script also includes example usage and test cases to demonstrate the function's behavior.