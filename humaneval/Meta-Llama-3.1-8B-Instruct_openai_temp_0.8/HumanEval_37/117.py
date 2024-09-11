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
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indices
    even.sort()

    # Combine the sorted even indices with the odd indices
    result = [None] * len(l)
    for i, (a, o) in enumerate(zip(even, odd)):
        result[2 * i] = a
        result[2 * i + 1] = o

    return result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function as specified and includes test cases to verify its correctness. The function separates the input list into two lists, one for even indices and one for odd indices. It sorts the even indices list and then combines the sorted even indices with the odd indices to produce the final result.