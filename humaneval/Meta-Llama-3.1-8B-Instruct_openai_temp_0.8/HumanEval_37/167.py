```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    Args:
        l (list): A list of elements.
    Returns:
        list: A new list with even indices sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    return [x if i % 2!= 0 else even_indices[i // 2] for i, x in enumerate(l)]

# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

In this script, we first create a list `even_indices` that contains the elements of the input list `l` at even indices, sorted in ascending order. Then we use a list comprehension to create the new list `l'` where the elements at even indices are taken from the `even_indices` list and the elements at odd indices are taken from the input list `l` unchanged. The result is a list `l'` that is identical to `l` at odd indices, but with the elements at even indices sorted.