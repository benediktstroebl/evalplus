```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list with even indices, otherwise the same as the input list.
    """
    # Separate the even and odd indices into two separate lists
    even = [l[i] for i in range(0, len(l), 2)]
    odd = [l[i] for i in range(1, len(l), 2)]

    # Sort the list of values at even indices
    even.sort()

    # Combine the sorted even values with the odd values
    result = [i if idx % 2!= 0 else j for idx, (i, j) in enumerate(zip(odd, even))]

    return result

# Test cases
print(sort_even([1, 2, 3]))
# Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Expected output: [3, 6, 5, 4]
```
This script defines a function `sort_even` that takes a list `l` and returns a new list where the even indices are sorted, while the odd indices remain the same. It achieves this by separating the even and odd indices into two lists, sorting the list of even values, and then combining them with the odd values. The test cases demonstrate the function's behavior on the provided examples.