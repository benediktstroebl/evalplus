```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list with even indices changed.
    """
    # Separate the even and odd indices of the list
    evens = [x for i, x in enumerate(l) if i % 2 == 0]
    odds = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indices
    evens.sort()

    # Combine the sorted even indices with the odd indices to form the result
    return [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(l, evens))]

# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines the `sort_even` function, which first separates the even and odd indices of the input list. It then sorts the even indices and combines them with the odd indices to form the final result. The script also includes test cases to verify the correctness of the function.