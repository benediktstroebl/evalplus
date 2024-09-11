```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list
    
    Returns:
    list: The sorted list according to the problem statement
    """
    # Separate even and odd elements into two lists
    even_elements = l[0::2]
    odd_elements = l[1::2]
    
    # Sort the even elements
    sorted_even_elements = sorted(even_elements)
    
    # Create the output list with the sorted even elements
    output = [None] * len(l)
    for i in range(0, len(l), 2):
        output[i] = sorted_even_elements[i // 2]
    for i in range(1, len(l), 2):
        output[i] = odd_elements[i // 2]
    
    return output

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

In this script, I first separate the even and odd elements into two separate lists. Then I sort the even elements. Finally, I create the output list with the sorted even elements at the even indices and the odd elements at the odd indices. This way, the output list is identical to the input list in the odd indices, and the values at the even indices are sorted.