Here's a self-contained Python script that uses the set intersection method to solve the problem:
```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.

    Returns:
        list: A sorted list of unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert lists to sets for efficient lookup and intersection
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets
    common_elements = set1 & set2

    # Convert the result back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Test the function
if __name__ == "__main__":
    print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
    print(common([5, 3, 2, 8], [3, 2]))
```
This script uses the `set` data type to efficiently find the intersection of the two input lists. The result is then converted back to a list and sorted before being returned. The test cases are included at the end of the script to verify that the function behaves as expected.