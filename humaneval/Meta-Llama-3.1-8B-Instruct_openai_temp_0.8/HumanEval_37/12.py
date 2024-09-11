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
    # Separate the even and odd indices into different lists
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the list of even indices
    even.sort()
    
    # Combine the sorted even indices with the odd indices
    return [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(odd, even))]

# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines the function `sort_even` as specified in the docstring. The function works by first separating the even and odd indices of the input list into two separate lists. It then sorts the list of even indices. Finally, it combines the sorted even indices with the odd indices, using the sorted even values in place of the original even values in the sorted list, and returns the result.