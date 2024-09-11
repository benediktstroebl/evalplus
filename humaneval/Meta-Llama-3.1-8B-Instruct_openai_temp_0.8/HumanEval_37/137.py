```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): Input list

    Returns:
        list: Modified list with even indices sorted
    """
    # Separate even and odd indices from the input list
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the values at even indices
    sorted_even_indices = sorted(even_indices)

    # Combine the sorted even indices with the odd indices
    sorted_l = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            sorted_l.append(sorted_even_indices[even_index])
            even_index += 1
        else:
            sorted_l.append(odd_indices[i // 2])

    return sorted_l


# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function, which takes a list `l` as input and returns a new list `l'` with the same values at odd indices but sorted values at even indices. It uses list comprehensions to separate the even and odd indices from the input list and then combines them back into a single list, replacing the even indices with the sorted values.