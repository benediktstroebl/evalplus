```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the even and odd indicies
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the values at even indicies
    even.sort()
    
    # Combine the sorted even values with the odd values
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even.pop(0))
        else:
            result.append(odd.pop(0))
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` and returns a new list where the values at even indicies are sorted. The function first separates the even and odd indicies of the input list using list comprehensions. It then sorts the values at the even indicies. Finally, it combines the sorted even values with the odd values in the correct order to form the output list.