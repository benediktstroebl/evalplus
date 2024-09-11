Here's a Python function that meets the requirements:
```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): A list of values.

    Returns:
        list: The sorted list according to the problem statement.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    even_values = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    return [x if i % 2!= 0 else even_values[i // 2] for i, x in enumerate(l)]
```
In this script, we use a list comprehension to create a list of even-indexed values from the input list `l`. We then sort this list of even values.

To create the output list `l'`, we use another list comprehension. We iterate over the indices and values of the input list `l`, and for each even index, we replace the value with the corresponding value from the sorted list of even values. For odd indices, we keep the original value. 

The expression `i // 2` is used to access the even-indexed values from the sorted list, because we want to map each even index in the original list to the corresponding even value in the sorted list.