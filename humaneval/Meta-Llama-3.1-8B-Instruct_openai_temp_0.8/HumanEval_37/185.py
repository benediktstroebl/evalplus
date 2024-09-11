```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): Input list

    Returns:
        list: List with even indices sorted and odd indices unchanged
    """
    # Separate even and odd indices
    even = [l[i] for i in range(0, len(l), 2)]
    odd = [l[i] for i in range(1, len(l), 2)]

    # Sort the even indices
    even.sort()

    # Combine the sorted even and unchanged odd indices
    return [even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(l))]


# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script takes a list as input, separates its even and odd indices, sorts the even indices, and then combines them with the unchanged odd indices to form the output list. The `//` operator performs integer division, which is used to determine the index in the sorted `even` list. The `%` operator is used to check if the current index is even or odd.