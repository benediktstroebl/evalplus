```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list
    
    Returns:
    list: The modified list with even indicies sorted
    
    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate even and odd indicies into two lists
    even indicies = [i for i, _ in enumerate(l) if i % 2 == 0]
    odd indicies = [i for i, _ in enumerate(l) if i % 2!= 0]
    
    # Get the values at even and odd indicies
    even_values = [l[i] for i in even indicies]
    odd_values = [l[i] for i in odd indicies]
    
    # Sort the even values
    even_values.sort()
    
    # Create the resulting list with even indicies sorted
    result = [even_values[i//2] if i % 2 == 0 else odd_values[i//2] for i in range(len(l))]
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script takes a list as input, separates the even and odd indicies into two lists, gets the values at these indicies, sorts the even values, and then combines them back into the original list with even indicies sorted. The resulting list is then returned.