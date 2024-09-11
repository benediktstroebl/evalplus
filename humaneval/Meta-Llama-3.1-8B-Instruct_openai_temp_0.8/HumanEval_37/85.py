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

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the even and odd indexed elements
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indexed elements
    even.sort()

    # Combine the sorted even elements with the odd elements
    result = [None] * len(l)
    for i, x in enumerate(even):
        result[i * 2] = x
    for i, x in enumerate(odd):
        result[i * 2 + 1] = x

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input, separates the even and odd indexed elements, sorts the even indexed elements, and then combines them with the odd elements to produce the output list. The function is then tested with the provided examples.