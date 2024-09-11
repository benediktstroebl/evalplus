```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list.
    """
    # Separate even and odd elements
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort even elements
    even.sort()
    
    # Combine sorted even and odd elements
    result = []
    for i, (e, o) in enumerate(zip(even, odd)):
        result.append(e if i % 2 == 0 else o)
    
    return result


# Test cases
print(sort_even([1, 2, 3]))
# Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Expected output: [3, 6, 5, 4]
```