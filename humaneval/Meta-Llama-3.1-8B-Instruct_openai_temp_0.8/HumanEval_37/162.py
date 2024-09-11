```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem description.
    """
    # Separate the values at even and odd indices
    even_values = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_values = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even values
    even_values.sort()

    # Combine the sorted even values and the odd values
    result = []
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even_values.pop(0))
        else:
            result.append(x)

    return result

# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` and returns a list `l'` such that `l'` is identical to `l` in the odd indices, while its values at the even indices are equal to the values of the even indices of `l`, but sorted. The test cases at the end of the script demonstrate the function's correctness.