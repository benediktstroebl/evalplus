```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem description.
    """
    # Use list comprehension to create a new list where values at odd indices are left unchanged
    # and values at even indices are sorted.
    return [x if i % 2!= 0 else sorted([y for y in l if i % 2 == 0])[i // 2] for i, x in enumerate(l)]


# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the elements at even indices are sorted based on the original elements at the same indices. The function uses list comprehension to achieve this. It then tests this function with the provided test cases.