```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list
    
    Returns:
        list: The modified list according to the problem description
    """
    even_sorted = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    return [x if i % 2!= 0 else even_sorted[i // 2] for i, x in enumerate(l)]

# Test the function
print(sort_even([1, 2, 3])) # [1, 2, 3]
print(sort_even([5, 6, 3, 4])) # [3, 6, 5, 4]
```

This script uses list comprehension to create a list of the values at the even indices, sorts it, and then replaces the values at the even indices in the original list with the sorted values. The `enumerate` function is used to get both the index and the value of each element in the list, and the modulo operator (`%`) is used to determine whether an index is even or odd.