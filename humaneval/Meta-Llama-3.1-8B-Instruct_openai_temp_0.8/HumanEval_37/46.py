```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): A list of elements to be sorted.

    Returns:
        list: A list where even indices are sorted.
    """
    even_sorted = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    return [x if i % 2!= 0 else even_sorted[i // 2] for i, x in enumerate(l)]

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the even indices are sorted. It first creates a new list `even_sorted` containing the elements at even indices from the original list, sorted in ascending order. Then it uses list comprehension to create the final list, where elements at even indices are replaced with their sorted counterparts. The `//` operator is used for integer division to get the index of the element in `even_sorted` that corresponds to the current index in the original list.