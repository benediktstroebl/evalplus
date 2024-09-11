**Sorting Even Indices in a List**
======================================

Here's a Python function that sorts the elements at even indices while keeping the elements at odd indices unchanged.

```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the even and odd indexed elements into two lists
    even_indexed = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_indexed = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indexed elements
    even_indexed.sort()

    # Combine the sorted even indexed elements with the odd indexed elements
    result = [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(odd_indexed, even_indexed))]

    return result
```

You can use this function to sort the even indices of a list while keeping the odd indices unchanged.