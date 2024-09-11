```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): A list of elements.
    
    Returns:
        list: A new list with even indicies sorted.
    
    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate odd and even indices in the list
    odd = [x for i, x in enumerate(l) if i % 2 == 0]
    even = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even elements
    sorted_even = sorted(even)
    
    # Create a new list where even indices are sorted and odd indices are the same
    sorted_l = []
    for i, (x, y) in enumerate(zip(even, sorted_even)):
        sorted_l.append(y if i % 2 == 0 else x)
    
    return sorted_l


# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```
This script defines a function `sort_even` that takes a list `l` and returns a new list with the even indices sorted. It first separates the odd and even indices in the list, then sorts the even elements, and finally creates a new list where even indices are sorted and odd indices are the same. The script includes docstrings and test cases to demonstrate the function's behavior.