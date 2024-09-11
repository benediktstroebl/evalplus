```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indices sorted.
    """
    # Separate the elements at even and odd indices
    even_elements = l[::2]
    odd_elements = l[1::2]

    # Sort the elements at even indices
    even_elements.sort()

    # Combine the elements at odd indices and the sorted elements at even indices
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_elements[i // 2])
        else:
            result.append(odd_elements[i // 2])

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function that takes a list `l` and returns a new list with the even indices sorted. It then tests this function with the provided examples.