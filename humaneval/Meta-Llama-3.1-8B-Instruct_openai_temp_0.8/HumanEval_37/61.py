```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list
    
    Returns:
        list: The modified list with even indicies sorted
    """
    # Separate even and odd indices of the list
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]
    
    # Sort the even indices
    even.sort()
    
    # Initialize the result list
    result = []
    
    # Populate the result list with the sorted even and original odd values
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even[i // 2])
        else:
            result.append(odd[i // 2])
    
    return result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function that meets the requirements. It first separates the even and odd indices of the input list into two separate lists. It then sorts the list of even indices. Finally, it constructs a new list by interleaving the sorted even indices and the original odd indices, as specified in the problem statement. The script includes test cases to verify the function's correctness.