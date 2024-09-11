```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.
    """
    # Separate the even and odd indices
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even.sort()

    # Combine the sorted even indices with the odd indices
    result = [None] * len(l)
    for i in range(len(even)):
        result[2 * i] = even[i]
    for i in range(len(odd)):
        result[2 * i + 1] = odd[i]

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` and returns a new list where the values at even indices are sorted, and the values at odd indices remain unchanged. The function uses list comprehensions to separate the even and odd indices, sorts the even indices, and then combines them back into a single list. The result is returned by the function. The script also includes test cases to verify that the function works correctly.