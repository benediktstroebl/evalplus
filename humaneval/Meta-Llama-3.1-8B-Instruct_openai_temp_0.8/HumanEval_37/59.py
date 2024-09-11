```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.
    """
    # Sort the even indices of the list
    even_indices = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the original list and append the correct value to the result
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indices[i // 2])
        else:
            result.append(l[i])
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input, sorts the elements at even indices, and returns a new list where the elements at even indices are the sorted ones from the original list, while the elements at odd indices remain unchanged. The function uses list comprehension to generate the sorted even indices and another loop to construct the resulting list. The script also includes test cases to verify the correctness of the function.