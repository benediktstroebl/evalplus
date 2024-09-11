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
    # Separate the list into two lists: one for even indices and one for odd indices
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the list of values at even indices
    even_indices.sort()

    # Combine the two lists back into one
    result = []
    for i, (e, o) in enumerate(zip(even_indices, odd_indices)):
        result.append(e if i % 2 == 0 else o)

    # Add any remaining odd indices
    result += odd_indices[len(even_indices):]

    return result


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input, separates its elements into two lists based on their indices, sorts the list of even-indexed elements, and then combines the two lists back into one. The elements at odd indices are left unchanged, while the elements at even indices are replaced by the sorted values. The function returns the resulting list.