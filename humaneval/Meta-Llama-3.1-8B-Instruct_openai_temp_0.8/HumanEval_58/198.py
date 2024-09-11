Here is a Python script that implements the `common` function as specified:
```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    common_list = sorted(list(common_elements))

    return common_list

# Test the function with the provided examples
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```
This script uses the `set` data structure to efficiently find the common elements between the two input lists. The `&` operator is used to compute the intersection of the two sets, and the resulting set is then converted back to a list and sorted using the `sorted` function. The `common_list` is then returned as the result of the function.