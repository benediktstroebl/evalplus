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
    # Separate the list into even and odd indexed elements
    even_indexed = [value for index, value in enumerate(l) if index % 2 == 0]
    odd_indexed = [value for index, value in enumerate(l) if index % 2!= 0]

    # Sort the even indexed elements
    even_indexed.sort()

    # Combine the sorted even indexed elements with the odd indexed elements
    return odd_indexed + even_indexed

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script uses list comprehension to separate the input list into two lists, one containing the even indexed elements and the other containing the odd indexed elements. It then sorts the even indexed elements using the `sort` method. Finally, it combines the sorted even indexed elements with the odd indexed elements in the correct order to produce the desired output.