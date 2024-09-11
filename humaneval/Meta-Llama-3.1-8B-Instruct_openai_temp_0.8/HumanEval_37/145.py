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
    # Separate the list into two lists: one with even indices and one with odd indices
    even_indices = l[::2]
    odd_indices = l[1::2]

    # Sort the list with even indices
    sorted_even = sorted(even_indices)

    # Combine the sorted list with odd indices and the sorted list with even indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even[i // 2])
        else:
            result.append(odd_indices[i // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input and returns a list that meets the specified conditions. It first separates the input list into two lists, one with even indices and one with odd indices. It then sorts the list with even indices and combines them with the list with odd indices to produce the final result. The test cases at the end demonstrate the function's correctness.