```python
def sort_third(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, 
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The transformed list.
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(l) if j % 3 == 0])[k] 
            for k, i, x in enumerate(l)]

# Test the function
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script defines a function `sort_third` that takes a list `l` as input and returns a new list where elements at indices divisible by 3 are sorted. The function uses a list comprehension to iterate over the input list, checking the index of each element for divisibility by 3. If the index is not divisible by 3, the element is left unchanged. If the index is divisible by 3, the element is replaced with the corresponding sorted element from the list of elements at indices divisible by 3. The function is then tested with the example inputs provided in the docstring.