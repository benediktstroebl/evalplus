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

    Example:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the list into two lists: one for even indices and one for odd indices
    even_indices = l[::2]
    odd_indices = l[1::2]

    # Sort the list for even indices
    sorted_even = sorted(even_indices)

    # Combine the sorted even list with the odd list
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even[i // 2])
        else:
            result.append(odd_indices[i // 2])

    return result

# Example usage:
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the elements at even indices are sorted. The function first separates the list into two lists: one for even indices and one for odd indices. It then sorts the list for even indices. Finally, it combines the sorted even list with the odd list, placing the sorted elements at even indices and the original elements at odd indices in the resulting list.