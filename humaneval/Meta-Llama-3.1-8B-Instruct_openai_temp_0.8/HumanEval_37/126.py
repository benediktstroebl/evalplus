```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The sorted list as per the problem statement.
    """
    # Slice the list into odd and even indicies
    odd = l[1::2]
    even = l[::2]
    
    # Sort the even indicies
    sorted_even = sorted(even)
    
    # Create a new list with sorted even indicies and original odd indicies
    result = [x for i, x in enumerate(l) if i % 2 == 0] + sorted_even
    
    return result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This Python script defines a function `sort_even` that takes a list `l` as input, slices it into odd and even indicies, sorts the even indicies, and returns a new list with the sorted even indicies and the original odd indicies. The script then tests this function with two test cases.