```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem specification.
    """
    # Separate even and odd indicies
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indicies
    even.sort()

    # Combine the sorted even indicies and odd indicies
    result = []
    even_index = 0
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even[even_index])
            even_index += 1
        else:
            result.append(x)

    return result


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script first separates the list into two lists: one for the even indicies and one for the odd indicies. It then sorts the list for the even indicies. After that, it combines the sorted list for the even indicies and the list for the odd indicies to form the final result according to the problem specification.