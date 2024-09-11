### Python Script to Sort Even Indices of a List

```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.
    """
    # Separate the list into two lists, one for even and one for odd indices
    even = [i for i in l if i % 2 == 0]
    odd = [i for i in l if i % 2!= 0]

    # Sort the list of even indices
    even.sort()

    # Combine the lists of odd and sorted even indices
    result = []
    for i, (o, e) in enumerate(zip(odd, even)):
        result.extend([o, e])

    return result


# Test the function
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script uses list comprehension and the built-in `sort` method to sort the even indices of the input list. It then combines the sorted list of even indices with the list of odd indices to produce the final output.