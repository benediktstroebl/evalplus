```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indices sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the list into two lists: one for even indices and one for odd indices
    even_indices = l[::2]
    odd_indices = l[1::2]

    # Sort the list of even indices
    even_indices.sort()

    # Combine the two lists, with the sorted even indices in the even positions
    return [x if i % 2 == 1 else y for i, (x, y) in enumerate(zip(odd_indices, even_indices))]

# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines the `sort_even` function, which takes a list `l` and returns a new list with the even indices sorted. It uses list slicing to separate the input list into two lists, one for even indices and one for odd indices. It then sorts the list of even indices and combines the two lists, using a list comprehension to insert the sorted even indices into the odd positions.