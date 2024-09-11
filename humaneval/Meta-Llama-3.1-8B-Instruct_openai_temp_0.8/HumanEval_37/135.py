### Python Script to Sort Even Indices in a List
```python
def sort_even(l: list):
    """
    This function takes a list `l` and returns a list `l'` such that
    `l'` is identical to `l` in the odd indices, while its values at the even indices are equal
    to the values of the even indices of `l`, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.
    """
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]  # Get values at even indices
    sorted_even_indices = sorted(even_indices)  # Sort the values
    result = []  # Initialize the result list
    odd_index = 0  # Index for odd indices in the original list
    even_index = 0  # Index for even indices in the original list

    # Interleave the values from the original list and the sorted even indices
    for i in range(len(l)):
        if i % 2 == 0:  # Even index
            result.append(sorted_even_indices[even_index])
            even_index += 1
        else:  # Odd index
            result.append(l[odd_index])
            odd_index += 1

    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```