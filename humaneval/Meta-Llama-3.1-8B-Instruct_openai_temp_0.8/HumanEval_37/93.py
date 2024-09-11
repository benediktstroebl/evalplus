```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The modified list with even indices sorted
    """
    # Separate the list into two lists: odd and even indexed values
    odd = [value for i, value in enumerate(l) if i % 2!= 0]
    even = [value for i, value in enumerate(l) if i % 2 == 0]

    # Sort the even indexed values
    even.sort()

    # Combine the sorted even indexed values with the odd indexed values
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

This script uses list comprehensions to separate the input list into two lists: one for odd indexed values and one for even indexed values. It then sorts the even indexed values and combines them with the odd indexed values in the correct order. The result is a new list that meets the problem's requirements.