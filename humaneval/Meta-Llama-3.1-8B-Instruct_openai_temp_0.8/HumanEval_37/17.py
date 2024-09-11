```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem's requirements.
    """
    # Separate even and odd indexed elements
    even_elements = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_elements = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indexed elements
    even_elements.sort()

    # Combine the sorted even indexed elements with the odd indexed elements
    result = [None] * len(l)
    for i, x in enumerate(l):
        if i % 2 == 0:
            result[i] = even_elements.pop(0)
        else:
            result[i] = x

    return result


# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

In this script, we first separate the even and odd indexed elements into two lists. Then we sort the even indexed elements using the `sort()` method. Finally, we combine the sorted even indexed elements with the odd indexed elements in the original order, but now with the sorted even indexed elements. The result is stored in the `result` list, which is then returned by the function.