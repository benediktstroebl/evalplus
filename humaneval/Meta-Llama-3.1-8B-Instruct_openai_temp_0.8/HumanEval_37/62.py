```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list to be sorted at even indices.

    Returns:
        list: The list with even indicies sorted.
    """
    # Separate the even and odd indices
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even.sort()

    # Combine the sorted even and original odd indices
    result = [value if i % 2!= 0 else even_val for i, (value, even_val) in enumerate(zip(odd, even))]

    return result


# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```
This script defines the function `sort_even` as specified. It separates the even and odd indices of the input list, sorts the even indices, and then combines them with the original odd indices to return the sorted list at even indices. The test cases demonstrate its functionality.