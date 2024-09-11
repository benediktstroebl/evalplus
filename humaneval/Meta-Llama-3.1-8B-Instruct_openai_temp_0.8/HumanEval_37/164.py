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
    # Separate even and odd indices
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even indices
    even.sort()

    # Combine the sorted even indices with the odd indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even[i // 2])
        else:
            result.append(odd[i // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` and returns a new list `l'` where the elements at even indices are sorted. The function uses list comprehensions to separate the elements at even and odd indices, sorts the even indices, and then combines them back into the result list. The test cases demonstrate the function's behavior.