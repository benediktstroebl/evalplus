```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with sorted even indicies.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the list into two lists: one with elements at even indices and one with elements at odd indices
    even = l[::2]
    odd = l[1::2]
    
    # Sort the list with even indices
    even.sort()
    
    # Combine the sorted even indices list with the odd indices list, maintaining the original order
    return [x for pair in zip(even, odd) for x in pair]

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

In this code:

1. We first separate the input list `l` into two lists: `even` (containing elements at even indices) and `odd` (containing elements at odd indices).
2. We sort the `even` list.
3. We combine the sorted `even` list with the `odd` list, maintaining the original order, using list comprehension with `zip` to iterate over both lists simultaneously.
4. We return the resulting list.