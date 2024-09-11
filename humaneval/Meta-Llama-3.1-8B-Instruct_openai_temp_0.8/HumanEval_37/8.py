```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indices sorted.
    
    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    even_values = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    return [x if i % 2!= 0 else even_values[i // 2] for i, x in enumerate(l)]

# Testing the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script uses list comprehension to achieve the desired result. It first sorts the values at the even indices of the input list. Then, it creates a new list where values at the even indices are taken from the sorted list of even values, and values at the odd indices are the same as in the original list. The `enumerate` function is used to get both the index and the value of each element in the list, and the `if i % 2 == 0` condition is used to get the even indices. The result is a list with even indices sorted.