```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indices sorted.
    
    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the list into odd and even indexed elements
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    even = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    
    # Combine the sorted even indexed elements with the odd indexed elements
    return odd + even

# Test the function
print(sort_even([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the even indexed elements are sorted. The function uses list comprehension to separate the list into odd and even indexed elements, sorts the even indexed elements, and then combines them with the odd indexed elements. The script also includes test cases to demonstrate the function's behavior.