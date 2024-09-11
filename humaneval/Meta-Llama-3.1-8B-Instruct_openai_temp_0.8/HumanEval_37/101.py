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
    # Separate the list into two lists, one for even indices and one for odd.
    even_indices = l[::2]
    odd_indices = l[1::2]
    
    # Sort the list of values at even indices.
    sorted_even_indices = sorted(even_indices)
    
    # Combine the two lists, replacing the values at even indices with the sorted values.
    result = [x if i % 2 == 1 else sorted_even_indices[i // 2] for i, x in enumerate(l)]
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` and returns a new list where the even indices of `l` are replaced with the values at the corresponding even indices of `l`, but in sorted order. The function uses list slicing to separate the input list into two lists, one for even indices and one for odd indices, sorts the list of values at even indices, and then combines the two lists using a list comprehension. The script includes two test cases to demonstrate the function's behavior.