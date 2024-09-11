```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
    l (list): The input list.
    
    Returns:
    list: A new list with even indices sorted.
    """
    
    # Separate the even and odd indices of the list
    even_idx = [i for i, _ in enumerate(l) if i % 2 == 0]
    odd_idx = [i for i, _ in enumerate(l) if i % 2!= 0]
    
    # Sort the values at even indices
    even_values = sorted([l[i] for i in even_idx])
    
    # Create the new list with even indices sorted and odd indices unchanged
    new_list = [l[i] if i % 2!= 0 else even_values[i // 2] for i in range(len(l))]
    
    return new_list


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function, which takes a list `l` as input and returns a new list with even indices sorted. The test cases are then executed to demonstrate the function's correctness.