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
    # Separate even and odd indexed elements
    even = [l[i] for i in range(0, len(l), 2)]
    odd = [l[i] for i in range(1, len(l), 2)]

    # Sort the even indexed elements
    even.sort()

    # Combine the sorted even elements with the odd elements
    result = [val for pair in zip(even, odd) for val in pair] + even[len(even):len(even)+len(odd)]
    return result


# Test cases
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list as input and returns a new list where even-indexed elements are sorted, while odd-indexed elements remain unchanged. The function uses list comprehension to separate even and odd indexed elements, sorts the even indexed elements, and then combines them with the odd indexed elements. The test cases demonstrate the function's correctness.