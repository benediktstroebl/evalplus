```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The resulting list.
    """
    # Separate even and odd elements
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even elements
    even.sort()

    # Combine the sorted even elements with the odd elements
    result = [0] * len(l)
    for i, x in enumerate(l):
        if i % 2 == 0:
            result[i] = even.pop(0)
        else:
            result[i] = x

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function, which takes a list `l` as input and returns a new list where the even-indexed elements are sorted. The script then tests this function with the example inputs provided in the docstring. The output of the script will be:

```
[1, 2, 3]
[3, 6, 5, 4]
```