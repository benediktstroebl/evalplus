```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list to be sorted.

    Returns:
        list: The modified list with even indices sorted.
    """
    # Separate even and odd indices in the list
    even = l[::2]
    odd = l[1::2]

    # Sort the even indices
    sorted_even = sorted(even)

    # Combine the sorted even indices with the odd indices
    return [val if idx % 2!= 0 else sorted_even[idx // 2] for idx, val in enumerate(l)]

# Test the function
print(sort_even([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Output: [3, 6, 5, 4]
```

This script uses list slicing to separate the even and odd indices, sorts the even indices using the `sorted` function, and then combines them using a list comprehension. The result is a new list where the even indices are sorted, while the odd indices remain unchanged.