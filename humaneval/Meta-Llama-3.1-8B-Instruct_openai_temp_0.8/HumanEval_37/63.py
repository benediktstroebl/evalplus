```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.
    """
    # Separate the list into even and odd indices
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even_indices.sort()

    # Create the new list by alternating between odd and even indices
    result = []
    while even_indices or odd_indices:
        if even_indices:
            result.append(even_indices.pop(0))
        if odd_indices:
            result.append(odd_indices.pop(0))

    return result

# Test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This code defines the `sort_even` function, which takes a list `l` as input. It separates the list into two lists, `even_indices` and `odd_indices`, based on their indices. Then, it sorts `even_indices`. Finally, it creates a new list by alternating between the sorted `even_indices` and the `odd_indices`. The function returns this new list.

The last two lines of the code test the function with the provided example inputs.