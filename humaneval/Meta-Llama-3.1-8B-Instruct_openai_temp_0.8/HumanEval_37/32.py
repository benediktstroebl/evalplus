```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list
    
    Returns:
    list: The modified list
    """
    # Separate even and odd indices
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2!= 0]
    
    # Get values at even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]
    
    # Sort the even values
    sorted_even_values = sorted(even_values)
    
    # Combine the sorted even values with the odd values
    result = [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(odd_values, sorted_even_values))]
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script first separates the even and odd indices of the input list. Then, it gets the values at these indices and sorts the values at the even indices. Finally, it combines the sorted even values with the odd values to produce the output list.