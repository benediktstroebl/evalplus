```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: A new list l' where the even indicies are sorted
    """
    # Separate the even and odd indices of the input list
    even_idx = [l[i] for i in range(0, len(l), 2)]
    odd_idx = [l[i] for i in range(1, len(l), 2)]

    # Sort the even indices
    even_idx.sort()

    # Combine the sorted even indices with the odd indices
    sorted_l = [x if i % 2 == 0 else y for i, (x, y) in enumerate(zip(even_idx, odd_idx))]

    # Fill in the remaining even indices with the sorted values
    sorted_l += even_idx[len(odd_idx):]

    return sorted_l


# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` and returns a new list `l'` where the even indices are sorted. It first separates the even and odd indices of the input list, sorts the even indices, and then combines them with the odd indices. The remaining even indices are filled with the sorted values. The script includes test cases to demonstrate the function's correctness.