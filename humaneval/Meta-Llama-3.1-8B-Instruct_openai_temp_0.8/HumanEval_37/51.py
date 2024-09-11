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
    # Separate even indices values into a new list
    even_values = [val for i, val in enumerate(l) if i % 2 == 0]
    
    # Sort the even values
    even_values.sort()
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize two pointers, one for the input list and one for the sorted even values
    i, j = 0, 0
    
    # Iterate over the input list
    for k in range(len(l)):
        # If the current index is even, append the smallest even value
        if k % 2 == 0:
            result.append(even_values[j])
            j += 1
        # If the current index is odd, append the value from the input list
        else:
            result.append(l[i])
            i += 1
    
    return result

# Test the function
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

In this code, we first create a new list `even_values` containing only the values at even indices from the input list `l`. We then sort this list. Finally, we iterate over the input list and append the smallest even value to the result list when the current index is even, and append the value from the input list when the current index is odd.