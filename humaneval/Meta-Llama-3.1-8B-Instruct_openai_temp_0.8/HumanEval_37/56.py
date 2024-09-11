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
    # Separate odd and even indices
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    
    # Sort even indices
    even_indices.sort()
    
    # Combine odd and sorted even indices
    result = []
    for i in range(len(l)):
        if i % 2!= 0:
            result.append(odd_indices.pop(0))
        else:
            result.append(even_indices.pop(0))
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input and returns a new list with the specified behavior. The test cases demonstrate the function's correctness.