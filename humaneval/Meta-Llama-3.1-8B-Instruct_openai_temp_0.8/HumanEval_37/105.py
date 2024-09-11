### Python Script to Sort Even Indices in a List
```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate even and odd indices
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even_indices.sort()

    # Combine the sorted even indices with the odd indices
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_indices[i // 2]
        else:
            result[i] = odd_indices[i // 2]

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```
This script first separates the even and odd indices from the input list using list comprehensions. It then sorts the even indices and combines them with the odd indices to form the final list. The result is a list where the even indices are sorted, while the odd indices remain unchanged.