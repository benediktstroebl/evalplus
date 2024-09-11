```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.
    """
    # Separate even and odd indices
    even_idx = [val for idx, val in enumerate(l) if idx % 2 == 0]
    odd_idx = [val for idx, val in enumerate(l) if idx % 2!= 0]
    
    # Sort the even indices
    even_idx.sort()
    
    # Combine the sorted even indices with the odd indices
    return [val for idx, val in zip(range(len(l)), even_idx + odd_idx)]

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the even indices are sorted. The function uses list comprehension and the `zip` function to create the new list. The test cases at the end demonstrate the function's behavior.