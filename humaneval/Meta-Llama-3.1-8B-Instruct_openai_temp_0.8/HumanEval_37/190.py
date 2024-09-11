```python
def sort_even(lst: list) -> list:
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of lst, but sorted.

    Args:
        lst (list): The input list.

    Returns:
        list: The modified list with even indices sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the even indices from the list
    even_indices = lst[::2]
    
    # Sort the even indices
    sorted_even_indices = sorted(even_indices)
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize two pointers to keep track of the current position in the list and the sorted list
    lst_pointer = 0
    sorted_lst_pointer = 0
    
    # Iterate over the original list with both odd and even indices
    for i in range(len(lst)):
        # If the index is even, append the current element from the sorted list
        if i % 2 == 0:
            result.append(sorted_even_indices[lst_pointer])
            lst_pointer += 1
        # If the index is odd, append the current element from the original list
        else:
            result.append(lst[lst_pointer])
            lst_pointer += 1
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script first separates the even indices from the input list and sorts them. Then it iterates over the original list, appending the sorted elements at even indices and the original elements at odd indices to the result list.