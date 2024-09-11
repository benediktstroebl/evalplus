```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the list into two lists, one for odd indices and one for even indices
    odds = [item for i, item in enumerate(l) if i % 2 == 0]
    evens = [item for i, item in enumerate(l) if i % 2!= 0]
    
    # Sort the list of even indices values
    sorted_evens = sorted(evens)
    
    # Combine the two lists, using the sorted even values for even indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_evens[i // 2])
        else:
            result.append(odds[i // 2])
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function as described, and includes two test cases to verify its correctness. It uses list comprehensions to separate the input list into two lists, one for odd indices and one for even indices. It then sorts the list of even indices values, and combines the two lists to obtain the final result.