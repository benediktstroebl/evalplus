```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indices sorted.
    
    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate odd and even indexed elements from the input list
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    
    # Sort the even indexed elements
    even.sort()
    
    # Combine the sorted even indexed elements with the odd indexed elements
    sorted_l = [v for pair in zip(even, odd) for v in pair]
    
    return sorted_l

# Example usage
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where even indices are sorted while odd indices remain unchanged. It first separates odd and even indexed elements using list comprehensions, sorts the even indexed elements using the `sort` method, and then combines the sorted even indexed elements with the odd indexed elements using the `zip` function. Finally, it returns the resulting list.