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

    Example:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate odd and even indices
    odd = l[1::2]
    even = l[::2]
    
    # Sort even indices
    even.sort()
    
    # Combine odd and sorted even indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even[i // 2])
        else:
            result.append(odd[i // 2])
            
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the function `sort_even` that takes a list `l` and returns a modified list with even indices sorted. It separates the odd and even indices, sorts the even indices, and then combines them back into the original order. The function is tested with the provided examples.