```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list.
    
    Returns:
    list: The modified list with even indices sorted.
    
    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate even and odd indices
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]
    
    # Sort even indices
    even_indices.sort()
    
    # Combine even and odd indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indices[i // 2])
        else:
            result.append(odd_indices[i // 2])
    
    return result

# Example usage:
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```
This script uses a list comprehension to separate even and odd indices from the input list. It then sorts the even indices and combines them with the odd indices in the desired order. The result is a list with even indices sorted.