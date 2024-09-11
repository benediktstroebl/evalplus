```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
    l (list): Input list of elements.
    
    Returns:
    list: Output list with even indicies sorted.
    """
    # Separate the even and odd indices
    even = [l[i] for i in range(0, len(l), 2)]
    odd = [l[i] for i in range(1, len(l), 2)]
    
    # Sort the even indices
    even.sort()
    
    # Combine the sorted even indices with the odd indices
    result = [even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(l))]
    
    return result

# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script uses list comprehension to separate the even and odd indices of the input list, sorts the even indices, and then combines the sorted even indices with the odd indices in the correct order. The result is a new list with the even indices sorted.