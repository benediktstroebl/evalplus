```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list.
    """
    # Separate even and odd indices
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indices
    even.sort()

    # Combine the sorted even indices with the odd indices
    result = [None] * len(l)
    for i, x in enumerate(l):
        if i % 2 == 0:
            result[i] = even.pop(0)
        else:
            result[i] = x

    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script first separates the input list into two lists: one for even indices and one for odd indices. Then it sorts the list of even indices. Finally, it combines the sorted even indices with the odd indices in the correct order.