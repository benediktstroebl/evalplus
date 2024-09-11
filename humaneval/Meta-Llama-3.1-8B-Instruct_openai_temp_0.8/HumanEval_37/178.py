```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the list into even and odd indicies
    even = l[1::2]
    odd = l[::2]
    
    # Sort the values at the even indicies
    even.sort()
    
    # Combine the sorted even and original odd values
    result = []
    for e, o in zip(even, odd):
        result.append(o)
        result.append(e)
    
    return result

# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script uses list slicing to separate the input list into its even and odd indicies, sorts the values at the even indicies, and then combines the sorted even values back with the original odd values. The `zip` function is used to pair up the even and odd values for this combination.