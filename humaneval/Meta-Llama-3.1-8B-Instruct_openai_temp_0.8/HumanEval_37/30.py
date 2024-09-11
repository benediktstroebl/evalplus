```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indicies sorted.
    """
    # Separate the even and odd indices of the list
    even_indices = [i for i, _ in enumerate(l) if i % 2 == 0]
    odd_indices = [i for i, _ in enumerate(l) if i % 2!= 0]
    
    # Get the values at the even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]
    
    # Sort the values at the even indices
    even_values.sort()
    
    # Construct the modified list with even indices sorted
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_values[even_indices.index(i)]
        else:
            result[i] = odd_values[odd_indices.index(i)]
    
    return result

# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script first separates the even and odd indices of the input list, then gets the corresponding values. It sorts the values at the even indices and constructs the modified list with even indices sorted. The test cases are also included to demonstrate the function's behavior.