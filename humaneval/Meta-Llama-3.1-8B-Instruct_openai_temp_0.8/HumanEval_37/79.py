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
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even indices
    even.sort()
    
    # Combine the even and odd lists
    result = []
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even.pop(0))
        else:
            result.append(odd.pop(0))
    
    # If there are remaining elements in even or odd, combine them to the result
    if even:
        result.extend(even)
    if odd:
        result.extend(odd)
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function and includes test cases at the end. The function takes a list `l` and separates its even and odd indices into two lists. It then sorts the even indices and combines the even and odd lists into a new list `result`. If there are remaining elements in the even or odd lists after the initial combination, they are appended to the `result` list. The function returns the `result` list.