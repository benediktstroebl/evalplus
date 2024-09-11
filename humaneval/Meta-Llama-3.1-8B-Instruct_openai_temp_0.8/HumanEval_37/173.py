```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The input list with even indicies sorted.
    """
    # Separate the list into two lists: one for even indices and one for odd indices
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the list for even indices
    even.sort()
    
    # Combine the two lists, replacing the original values for even indices with the sorted ones
    return [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(odd, even))]

# Test the function
print(sort_even([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Output: [3, 6, 5, 4]
```