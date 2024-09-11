```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list.
    """
    # Separate even and odd indices from the input list
    even_index_values = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_index_values = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the values at even indices
    sorted_even_index_values = sorted(even_index_values)

    # Combine the sorted even index values with the odd index values
    sorted_list = [x if i % 2!= 0 else y for i, x in enumerate(l) for y in sorted_even_index_values]

    return sorted_list


# Example use cases
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script accomplishes the task by first separating the values at even and odd indices into two separate lists. It then sorts the list of values at even indices. Finally, it combines the sorted even index values with the odd index values to produce the desired output list. The example use cases at the end demonstrate the function's behavior with two test cases.