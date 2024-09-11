```python
def sort_even(lst: list):
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the odd indices, while its values at the even indices are equal
    to the values of the even indices of lst, but sorted.

    Args:
        lst (list): The input list

    Returns:
        list: The modified list
    """
    # Separate even and odd indices
    even_indices = [i for i in range(len(lst)) if i % 2 == 0]
    odd_indices = [i for i in range(len(lst)) if i % 2!= 0]

    # Get values at even and odd indices
    even_values = [lst[i] for i in even_indices]
    odd_values = [lst[i] for i in odd_indices]

    # Sort the even values
    even_values.sort()

    # Combine the sorted even values with the odd values
    result = [0] * len(lst)
    for i, val in enumerate(even_values):
        result[even_indices[i]] = val
    for i, val in enumerate(odd_values):
        result[odd_indices[i]] = val

    return result


# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `lst` as input, separates its even and odd indices, sorts the values at the even indices, and combines the sorted even values with the odd values to produce the output list. The script includes two test cases to demonstrate the function's behavior.