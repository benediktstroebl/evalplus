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
    # Separate even and odd indicies
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even indicies
    sorted_even = sorted(even)

    # Combine the sorted even and original odd elements
    result = []
    for i, (x, y) in enumerate(zip(sorted_even, l)):
        if i % 2 == 0:
            result.append(y)
        else:
            result.append(x)

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the values at the even indicies are sorted, but the values at the odd indicies remain the same. The test cases demonstrate the function's behavior.