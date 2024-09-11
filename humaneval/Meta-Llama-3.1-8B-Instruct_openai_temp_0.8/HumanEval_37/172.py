```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list
    
    Returns:
    list: The sorted list according to the given criteria
    """
    # Separate the even and odd indices of the list
    evens = [x for i, x in enumerate(l) if i % 2 == 0]
    odds = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indices
    sorted_evens = sorted(evens)

    # Replace the even indices in the original list with the sorted even values
    sorted_l = [x if i % 2!= 0 else sorted_evens[i // 2] for i, x in enumerate(l)]

    return sorted_l

# Testing the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script does the following:

1. It separates the even and odd indices of the list l.
2. It sorts the even indices.
3. It replaces the even indices in the original list with the sorted even values.
4. It returns the sorted list according to the given criteria.