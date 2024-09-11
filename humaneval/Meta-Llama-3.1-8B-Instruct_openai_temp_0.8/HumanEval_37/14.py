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
    # Separate the even and odd indicies of the list
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even indicies
    even.sort()
    
    # Combine the sorted even and original odd indicies
    result = []
    for e, o in zip(even, odd):
        result.append(e)
        result.append(o)
    
    # If the length of the list is odd, append the last element
    if len(l) % 2!= 0:
        result.append(l[-1])
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function, which takes a list as input and returns a new list with the even indicies sorted. The function uses list comprehensions to separate the even and odd indicies, sorts the even indicies, and then combines the sorted even and original odd indicies into a new list. The script also includes test cases to verify the function's correctness.