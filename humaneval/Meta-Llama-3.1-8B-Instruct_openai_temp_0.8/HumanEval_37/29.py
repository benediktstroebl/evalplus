```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The modified list
    """
    # Separate the even and odd indexed elements into two lists
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indexed elements
    even.sort()

    # Combine the sorted even elements with the odd elements, maintaining the original order
    result = [x if i % 2!= 0 else y for i, x in enumerate(odd) for y in even]

    return result

# Test cases
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script uses list comprehension to create two lists: one for even indexed elements and one for odd indexed elements. It then sorts the even indexed elements and combines them with the odd indexed elements, maintaining the original order. The result is a new list that meets the required conditions.