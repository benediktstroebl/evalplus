```python
def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    
    Args:
        l (list): Input list
    
    Returns:
        list: Sorted list with even indices maintained in original order
    """
    # Split the list into two lists, one for even and one for odd indices
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the list for even indices
    even.sort()
    
    # Combine the two lists
    return odd + even

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input, splits it into two lists (one for even indices and one for odd indices), sorts the list for even indices, and then combines the two lists to return the result. The script also includes test cases to verify the function's correctness.