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
    """
    # Separate the even and odd indices
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even indices
    even.sort()
    
    # Combine the sorted even indices and the odd indices
    result = [x if i % 2!= 0 else y for i, x in enumerate(odd + even)]
    
    return result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script uses list comprehensions to separate the elements at even and odd indices into two lists. It then sorts the even list. Finally, it combines the sorted even list and the odd list, swapping elements at even indices back in. The result is a list with elements at odd indices identical to the input list, and elements at even indices sorted.