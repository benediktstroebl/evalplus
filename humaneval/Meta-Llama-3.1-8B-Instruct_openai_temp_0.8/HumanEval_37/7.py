```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The sorted list according to the problem statement
    """
    # Separate even and odd indices into two lists
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the list of even indices
    even_indices.sort()

    # Combine the sorted even indices with the odd indices
    result = [val if i % 2!= 0 else val for i, val in enumerate(even_indices + odd_indices)]

    return result


# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` and returns a new list where the even indices are sorted. It uses list comprehension to separate the even and odd indices, sorts the list of even indices, and then combines the two lists back together, replacing the even indices with the sorted values. The function is then tested with the provided example cases.