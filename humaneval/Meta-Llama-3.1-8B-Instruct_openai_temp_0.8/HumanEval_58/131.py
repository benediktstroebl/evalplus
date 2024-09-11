### Common Elements in Two Lists
#### Problem Statement

Find the sorted unique common elements between two lists.

#### Solution
```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    
    :param l1: The first list.
    :param l2: The second list.
    :return: A sorted list of unique common elements.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```
This script defines a function `common` that takes two lists as input, removes duplicates, finds the intersection of the two lists (i.e., the common elements), and returns the result as a sorted list. The example usage demonstrates the function's functionality with two sets of inputs.