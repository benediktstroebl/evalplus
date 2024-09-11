```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indicies sorted.
    """
    # Separate even and odd indices into two lists
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2!= 0]
    
    # Create a copy of the input list
    result = l.copy()
    
    # Sort the values at even indices (in the original list)
    sorted_even = sorted([l[i] for i in even_indices])
    
    # Replace the values at even indices in the result list with the sorted values
    for i in even_indices:
        result[i] = sorted_even[even_indices.index(i)]
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Output: [3, 6, 5, 4]
```

This script defines the function `sort_even` that takes a list `l` as input, separates its even and odd indices, and returns a new list where the values at even indices are sorted according to their original order in the list.