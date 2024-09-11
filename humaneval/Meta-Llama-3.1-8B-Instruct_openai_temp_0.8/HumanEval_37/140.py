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
    # Sort the even indices of the list
    even_indices = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    
    # Create a new list with the same odd indices as the original list
    result = [l[i] if i % 2!= 0 else even_indices[i // 2] for i in range(len(l))]
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list with the same elements at odd indices but with the elements at even indices sorted. It uses list comprehension to create a new list with the desired elements. The test cases at the end of the script demonstrate the function's behavior.