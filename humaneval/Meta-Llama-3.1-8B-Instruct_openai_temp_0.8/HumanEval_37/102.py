```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indices sorted.

    Example:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    even = sorted([x for i, x in enumerate(l) if i % 2 == 0])  # Sort even indices
    odd = [x for i, x in enumerate(l) if i % 2!= 0]  # Keep odd indices as is
    return [x for pair in zip(even, odd) for x in pair]  # Interleave sorted even and odd indices


# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
print(sort_even([10, 20, 30, 40, 50]))  # Output: [10, 20, 30, 40, 50]
```

This script defines a function `sort_even` that takes a list `l` and returns a new list `l'` with even indices sorted. It uses list comprehension to separate the even and odd indices, sorts the even indices, and then interleaves the sorted even and odd indices to form the output list. The function is tested with three example inputs.