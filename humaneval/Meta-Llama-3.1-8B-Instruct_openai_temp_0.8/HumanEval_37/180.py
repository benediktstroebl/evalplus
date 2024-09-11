```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indicies sorted.
    """
    even = [x for i, x in enumerate(l) if i % 2 == 0]  # Get even indicies
    even.sort()  # Sort the values at even indicies
    result = []  # Initialize the result list
    e_idx = 0  # Initialize the even index counter
    
    for i, x in enumerate(l):  # Iterate over the input list
        if i % 2 == 0:  # If the index is even
            result.append(even[e_idx])  # Append the sorted value
            e_idx += 1  # Increment the even index counter
        else:
            result.append(x)  # Append the value at odd index
    
    return result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function according to the provided specification. It uses list comprehension to get the values at even indices, sorts them, and then iterates over the input list to create the modified list with even indices sorted. The test cases are included at the end to verify the function's correctness.