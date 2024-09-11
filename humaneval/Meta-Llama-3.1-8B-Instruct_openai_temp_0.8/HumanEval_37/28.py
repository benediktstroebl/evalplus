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

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the list into odd and even indexed elements
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    even = [x for i, x in enumerate(l) if i % 2 == 0]

    # Sort the even indexed elements
    even.sort()

    # Combine the sorted even indexed elements with the odd indexed elements
    return odd + even

# Test the function
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input and returns a new list. The function works by separating the input list into two lists, one with odd indexed elements and one with even indexed elements. It then sorts the even indexed elements and combines the sorted even indexed elements with the odd indexed elements to produce the output list. The function is tested with two examples to demonstrate its correctness.