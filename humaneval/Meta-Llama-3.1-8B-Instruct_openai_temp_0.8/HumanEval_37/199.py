```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The transformed list.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Use list comprehension to create a new list with values at even indices sorted
    return [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(l, sorted(l)[::-1]))]

# Test the function
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script uses list comprehension to create a new list. It iterates over the input list with `enumerate` to get both the index and the value. If the index is odd, the value remains the same; if the index is even, the value is taken from the sorted list in reverse order. The `[::-1]` slice reverses the sorted list, so the even-index values are taken in reverse order, effectively sorting them.