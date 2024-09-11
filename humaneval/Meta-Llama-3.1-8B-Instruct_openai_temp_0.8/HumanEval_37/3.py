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
    """
    # Separate the list into two lists, one for odd indices and one for even indices
    odd = l[1::2]
    even = sorted(l[::2])

    # Combine the two lists, with values from even at even indices and values from odd at odd indices
    result = [even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(l))]

    return result


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function as described, and then tests it with the provided examples. The function uses list slicing and list comprehension to separate the list into odd and even index values, sort the even index values, and then combine them back into a single list.