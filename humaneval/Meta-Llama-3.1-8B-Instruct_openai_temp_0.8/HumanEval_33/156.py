```python
def sort_third(lst: list) -> list:
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the indices that are not divisible by three, 
    while its values at the indices that are divisible by three are equal 
    to the values of the corresponding indices of lst, but sorted.

    Args:
        lst (list): The input list.

    Returns:
        list: The modified list.
    """
    return [x if i % 3!= 0 else sorted([y for y in lst if i % 3 == 0])[i % 3] for i, x in enumerate(lst)]


# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script defines the function `sort_third` that takes a list as input and returns a new list where the elements at indices divisible by 3 are replaced with the sorted elements from the list at those indices. The `enumerate` function is used to get the index and value of each element in the list, and the `if` condition is used to filter the elements based on their indices. The sorted elements are then selected from the list using a list comprehension.