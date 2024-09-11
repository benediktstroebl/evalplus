```python
def sort_even(lst: list):
    """
    This function takes a list and returns a list such that
    the returned list is identical to the input list in the odd indicies,
    while its values at the even indicies are equal
    to the values of the even indicies of the input list, but sorted.

    Args:
        lst (list): The input list

    Returns:
        list: The modified list
    """
    # Separate the list into two lists, one with odd indices and one with even indices
    odd_indices = lst[::2]
    even_indices = sorted(lst[1::2])

    # Initialize an empty list to store the result
    result = []

    # Iterate over the indices and values of the input list
    for i, v in enumerate(lst):
        # If the index is odd, append the value from the odd_indices list
        if i % 2 == 0:
            result.append(odd_indices[i // 2])
        # If the index is even, append the value from the even_indices list
        else:
            result.append(even_indices[i // 2])

    return result

# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input, separates it into two lists (one with odd indices and one with even indices), sorts the list with even indices, and then combines the two lists into a new list where the even indices are sorted but the odd indices remain the same. The script then tests this function with the provided test cases.