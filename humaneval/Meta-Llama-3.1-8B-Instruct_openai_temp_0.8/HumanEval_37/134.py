```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indicies sorted.
    """
    # Separate the even and odd indices
    even_indices = [x for x in range(0, len(l), 2)]
    odd_indices = [x for x in range(1, len(l), 2)]
    
    # Get the values at even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]
    
    # Sort the even values
    sorted_even_values = sorted(even_values)
    
    # Replace the original even values with the sorted ones
    sorted_l = [sorted_even_values[i] if i in even_indices else odd_values[i] for i in range(len(l))]
    
    return sorted_l

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list with the even indices sorted. It first separates the even and odd indices, then gets the values at these indices, sorts the even values, and finally replaces the original even values with the sorted ones. The function is tested with the given examples.