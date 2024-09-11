```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: A new list where the even indices are sorted.
    """
    # Separate the elements at even and odd indices
    even_indices = l[::2]
    odd_indices = l[1::2]

    # Sort the elements at even indices
    sorted_even_indices = sorted(even_indices)

    # Combine the sorted even indices with the odd indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_indices[i // 2])
        else:
            result.append(odd_indices[i // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This Python script defines the `sort_even` function, which takes a list `l` as input. It separates the elements at even and odd indices, sorts the elements at even indices, and then combines them with the unsorted elements at odd indices in the correct order. The function returns this new list, which satisfies the problem's requirements. The test cases demonstrate the function's correctness.