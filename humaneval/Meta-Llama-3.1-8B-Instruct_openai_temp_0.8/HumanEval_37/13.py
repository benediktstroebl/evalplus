```python
def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The sorted list l'.
    """
    # Separate even and odd indexed elements
    even_indexed = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_indexed = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort even indexed elements
    even_indexed.sort()
    
    # Combine sorted even indexed elements with odd indexed elements
    result = []
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even_indexed.pop(0))
        else:
            result.append(x)
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines the `sort_even` function that takes a list `l` as input, separates the even and odd indexed elements, sorts the even indexed elements, and then combines them back into a list, maintaining the original odd indexed elements. The test cases are included at the end to demonstrate the function's behavior.