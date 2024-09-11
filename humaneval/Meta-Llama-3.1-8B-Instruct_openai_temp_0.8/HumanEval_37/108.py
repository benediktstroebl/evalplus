```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indicies sorted.
    """
    # Separate even and odd indices
    even_indices = [i for i, _ in enumerate(l) if i % 2 == 0]
    odd_indices = [i for i, _ in enumerate(l) if i % 2!= 0]

    # Get values at even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]

    # Sort values at even indices
    even_values.sort()

    # Combine sorted even values with odd values to form the result
    result = []
    for even, odd in zip(even_indices, even_values):
        result.append(l[odd])
        result.append(l[even])

    return result

# Example usage
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```