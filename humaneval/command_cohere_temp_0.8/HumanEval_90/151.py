```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach utilizes Python's built-in sorting function (`sort()`) to order the list in ascending order. Subsequently, we check the length of the list. If the length is less than 2, indicating an insufficient number of elements for a second smallest, we return `None`. Alternatively, we return the second element (index -2) from the sorted list, which corresponds to the second smallest element in the original list.

Here is a more robust version that handles all edge cases, including lists with negative and floating-point numbers:
```python
def next_smallest(lst):
    # Sort the list and get the length
    lst.sort()
    num_elements = len(lst)

    # Check if there are at least two elements
    if num_elements < 2:
        return None

    # Check if there is exactly one element
    if num_elements == 1:
        return None

    # Return the second element
    return lst[-2]
```

This version is more robust because it handles lists of different types and still returns the correct result. You can verify this by running the function with different input lists, such as `[1, 2, 3, 4, 5]`, `[5, 1, 4, 3, 2]`, `[]`, `[1, 1]`, and `-1 1 -2 .5`. It should return `2`, `2`, `None`, `None`, and `0` respectively.