```python
def sort_even(lst: list) -> list:
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of lst, but sorted.

    Args:
        lst (list): The input list

    Returns:
        list: The modified list
    """
    # Separate the even indicies from the list
    even_idx_values = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    
    # Sort the values at the even indicies
    sorted_even_idx_values = sorted(even_idx_values)
    
    # Create a new list where the values at the even indicies are sorted
    sorted_lst = [None] * len(lst)
    for i in range(len(lst)):
        if i % 2 == 0:
            sorted_lst[i] = sorted_even_idx_values.pop(0)
        else:
            sorted_lst[i] = lst[i]
    
    return sorted_lst

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input and returns a new list where the values at the even indicies are sorted. The function uses list comprehension to separate the values at the even indicies, sorts them using the built-in `sorted` function, and then creates a new list with the sorted values at the even indicies and the original values at the odd indicies. The script also includes test cases to demonstrate the function's behavior.