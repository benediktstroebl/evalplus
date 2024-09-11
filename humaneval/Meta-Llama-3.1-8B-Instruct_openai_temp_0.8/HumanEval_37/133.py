```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list to be sorted.

    Returns:
        list: The list with even indicies sorted.
    """
    # Separate odd and even indices
    odd = [l[i] for i in range(0, len(l), 2)]
    even = sorted([l[i] for i in range(1, len(l), 2)])

    # Combine the two lists
    sorted_l = []
    for i in range(len(l)):
        if i % 2 == 0:  # Even index
            sorted_l.append(even[i // 2])
        else:  # Odd index
            sorted_l.append(odd[i // 2])

    return sorted_l


# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input, separates the odd and even indices, sorts the even indices, and then combines them back into a single list. The function is then tested with the provided test cases.