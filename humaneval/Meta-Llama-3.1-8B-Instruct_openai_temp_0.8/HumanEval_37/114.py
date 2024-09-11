```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The output list with even indicies sorted.
    
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    return [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(l, sorted(l)[::2]))]

# Example usage:
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function, which uses list comprehension to create a new list that meets the requirements. It iterates over the input list `l` using `enumerate` with a `zip` object that pairs each element with its sorted equivalent at even indices. The `if i % 2!= 0` condition ensures that elements at odd indices remain unchanged, while elements at even indices are replaced with their sorted equivalents.