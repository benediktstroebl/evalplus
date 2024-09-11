```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Parameters:
    l1 (list): The first list.
    l2 (list): The second list.

    Returns:
    list: A sorted list of unique common elements.
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Use set intersection to find common elements
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    sorted_common_elements = sorted(list(common_elements))

    return sorted_common_elements

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])) 
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

In this code:

1.  We define a function `common(l1, l2)` that takes two lists as input.
2.  We convert the input lists to sets, which removes any duplicate elements and provides efficient lookup.
3.  We use the `&` operator to find the intersection of the two sets, which gives us the common elements.
4.  We convert the set of common elements back to a list and sort it using the `sorted()` function.
5.  We return the sorted list of common elements.
6.  We include test cases at the end to demonstrate the function's behavior.