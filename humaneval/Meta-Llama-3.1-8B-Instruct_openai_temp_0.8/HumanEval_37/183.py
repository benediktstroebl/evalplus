```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem statement.
    """
    # Separate the even and odd indices of the list
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even_indices.sort()

    # Combine the sorted even indices and the odd indices
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

This script uses list comprehension to separate the even and odd indices of the input list, sorts the even indices, and then combines them with the odd indices in the same order, resulting in a list where the even indices are sorted and the odd indices remain unchanged.