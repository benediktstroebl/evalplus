```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list
    
    Returns:
    list: The modified list with even indices sorted
    
    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the even and odd indices of the list
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]
    
    # Sort the even indices
    sorted_even_indices = sorted(even_indices)
    
    # Combine the sorted even indices with the odd indices to form the output list
    output_list = []
    for i, val in enumerate(l):
        if i % 2 == 0:
            output_list.append(sorted_even_indices.pop(0))
        else:
            output_list.append(val)
    
    return output_list

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list `l'` such that the even indices of `l'` contain the sorted even indices of `l`, while the odd indices of `l'` remain the same as `l`. The function uses list comprehensions to separate the even and odd indices of the input list, sorts the even indices, and then combines the sorted even indices with the odd indices to form the output list. The function is tested with the provided examples.