```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem description.

    Example:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate even and odd indices
    even = l[::2]
    odd = l[1::2]

    # Sort the list at even indices
    even.sort()

    # Combine the two lists
    return [even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(l))]


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` and returns a new list where the values at the even indices are equal to the values of the even indices of `l`, but sorted. The values at the odd indices remain the same. It then tests this function with the provided example cases.