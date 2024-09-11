```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the given conditions.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    even_indices = l[::2]  # Get values at even indices
    sorted_even_indices = sorted(even_indices)  # Sort values at even indices
    result = []  # Initialize the result list
    for i in range(len(l)):  # Iterate over the indices of the input list
        if i % 2 == 0:  # Check if the index is even
            result.append(sorted_even_indices[i // 2])  # Append the sorted value
        else:
            result.append(l[i])  # Append the original value
    return result  # Return the result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input and returns a new list where the values at even indices are sorted while the values at odd indices remain the same. The function uses list slicing to extract values at even indices, sorts them, and then constructs the result list by interleaving the sorted values with the original values at odd indices.