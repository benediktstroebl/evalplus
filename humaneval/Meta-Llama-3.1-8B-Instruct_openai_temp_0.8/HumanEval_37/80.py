```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate even and odd indices
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indices list
    even.sort()

    # Combine the sorted even indices with the odd indices
    result = [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(odd, even))]

    return result

# Test the function
print(sort_even([1, 2, 3]))
# [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# [3, 6, 5, 4]
```

This script uses list comprehension and the `enumerate` function to separate the even and odd indices from the input list. It then sorts the even indices list and combines it with the odd indices list using another list comprehension. The result is the modified list where the even indices are sorted.