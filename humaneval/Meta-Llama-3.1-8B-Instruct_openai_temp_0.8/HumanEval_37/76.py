```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indices sorted.
    """
    # Separate even and odd indices
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even_indices.sort()

    # Combine the even and odd indices back into a list
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indices[i // 2])
        else:
            result.append(odd_indices[i // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This code first separates the even and odd indices of the list into two separate lists. It then sorts the even indices. Finally, it combines the even and odd indices back into a list, with the even indices now sorted.