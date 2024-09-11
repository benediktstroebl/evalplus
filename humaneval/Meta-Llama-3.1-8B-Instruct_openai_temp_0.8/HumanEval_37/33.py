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
    # Separate the list into two lists, one for even and one for odd indices
    evens = [x for i, x in enumerate(l) if i % 2 == 0]
    odds = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even indices list in ascending order
    evens.sort()
    
    # Create the result list by alternating between the odd and even lists
    result = []
    for i in range(max(len(evens), len(odds))):
        if i < len(evens):
            result.append(evens[i])
        if i < len(odds):
            result.append(odds[i])
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script uses list comprehensions to separate the input list into two lists, one for even and one for odd indices. It then sorts the even indices list and uses another list comprehension to create the result list by alternating between the odd and even lists. The sorted even values are inserted into the even positions in the result list, and the odd values from the original list are inserted into the odd positions.