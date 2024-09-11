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
    # Separate the list into two lists, one for even indices and one for odd indices
    even_indices = l[::2]
    odd_indices = l[1::2]

    # Sort the list of even indices
    even_indices.sort()

    # Combine the two lists, alternating between odd and even indices
    result = [item for pair in zip(even_indices, odd_indices) for item in pair]
    result += even_indices[len(odd_indices):]  # Append any remaining even indices

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function, which takes a list as input and returns a new list where the even indices are sorted. The script also includes test cases to demonstrate the function's behavior.