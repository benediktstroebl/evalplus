```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    
    Parameters:
    l (list): The input list
    
    Returns:
    list: A new list with even indices sorted
    
    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the even and odd indices into two lists
    even_indices = l[::2]
    odd_indices = l[1::2]
    
    # Sort the even indices
    even_indices.sort()
    
    # Create a new list with the sorted even indices and the original odd indices
    new_list = [None] * len(l)
    new_list[::2] = even_indices
    new_list[1::2] = odd_indices
    
    return new_list

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list with the even indices sorted. The function first separates the even and odd indices into two lists, sorts the even indices, and then creates a new list with the sorted even indices and the original odd indices. The test cases at the end demonstrate the function's correctness.