```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The modified list with even indicies sorted
    """
    # Separate the even and odd indices of the list
    even_indices = [x for x in range(len(l)) if x % 2 == 0]
    odd_indices = [x for x in range(len(l)) if x % 2!= 0]

    # Get the values at the even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]

    # Sort the even values
    even_values.sort()

    # Combine the sorted even values with the odd values to get the result
    result = [0] * len(l)
    for i, val in zip(even_indices, even_values):
        result[i] = val
    for i, val in zip(odd_indices, odd_values):
        result[i] = val

    return result


# Test the function
print(sort_even([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input, separates the even and odd indices, sorts the values at the even indices, and combines them with the values at the odd indices to produce the output. The function is then tested with two example inputs.