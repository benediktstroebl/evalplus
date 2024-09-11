```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
    l (list): A list of elements.

    Returns:
    list: A list identical to l in the odd indicies, but with values at the even indicies sorted.

    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indiced = [x for i, x in enumerate(l) if i % 2 == 0]
    sorted_even_indiced = sorted(even_indiced)
    sorted_even_indiced_with_odd_values = []
    for i, x in enumerate(l):
        if i % 2 == 0:
            sorted_even_indiced_with_odd_values.append(sorted_even_indiced.pop(0))
        else:
            sorted_even_indiced_with_odd_values.append(x)
    return sorted_even_indiced_with_odd_values

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the function `sort_even` that takes a list `l` as input. It first separates the even indicied elements into a list `even_indiced`. Then it sorts this list. It then iterates over the original list, replacing the elements at even indicies with the corresponding sorted ones. The result is the sorted list according to the problem description. The script then tests the function with the provided examples.