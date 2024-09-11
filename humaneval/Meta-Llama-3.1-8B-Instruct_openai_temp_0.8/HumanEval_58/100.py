### Common Elements in Two Lists
#### Problem Description
This script finds the common elements between two lists, removes duplicates, and returns the sorted list.
#### Code
```python
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    return sorted(set(l1) & set(l2))

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```
#### Explanation
This script uses Python's built-in `set` data type to find the common elements. A set in Python is an unordered collection of unique elements. The `&` operator is used to find the intersection of two sets, i.e., the elements common to both sets.

After finding the common elements, we convert the resulting set back to a list and sort it using the `sorted` function.

Note that this script assumes that the input lists are lists of hashable types (like integers, strings, etc.). If the input lists contain unhashable types (like lists, dictionaries, etc.), this script will raise a `TypeError`.