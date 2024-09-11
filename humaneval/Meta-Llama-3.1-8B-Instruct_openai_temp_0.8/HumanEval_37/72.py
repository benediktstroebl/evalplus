```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The transformed list

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the even and odd indices of the list
    even = l[::2]
    odd = l[1::2]

    # Sort the even indices
    even.sort()

    # Combine the sorted even indices and the odd indices
    return [x for pair in zip(even, odd) for x in pair]


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` which takes a list `l` and returns a new list where the even indices are sorted, but the odd indices remain unchanged. It first separates the even and odd indices using slicing (`l[::2]` and `l[1::2]`), sorts the even indices, and then combines the sorted even indices and the odd indices using a list comprehension. The function is then tested with two examples.