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
    even_indices = [i for i, x in enumerate(l) if i % 2 == 0]
    odd_indices = [i for i, x in enumerate(l) if i % 2!= 0]

    # Sort values at even indices
    even_values = sorted([l[i] for i in even_indices])

    # Create the result list with even indices sorted
    result = [0] * len(l)
    for i, x in enumerate(l):
        if i % 2 == 0:
            result[i] = even_values.pop(0)
        else:
            result[i] = l[i]

    return result


# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that modifies the input list by sorting its even indices. It uses list comprehension to separate even and odd indices, sort the values at even indices, and then builds the result list by replacing the even-indexed values with their sorted versions. The script also includes test cases to verify the function's correctness.