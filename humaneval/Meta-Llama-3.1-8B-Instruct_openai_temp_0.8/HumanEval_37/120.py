```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem description.
    """
    # Separate the even and odd indices of the list
    even_indices = [x for x in range(len(l)) if x % 2 == 0]
    odd_indices = [x for x in range(len(l)) if x % 2!= 0]

    # Separate the even and odd values of the list
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]

    # Sort the even values
    even_values.sort()

    # Merge the sorted even values back into the list at their original even indices
    result = [None] * len(l)
    for i in even_indices:
        result[i] = even_values.pop(0)
    for i in odd_indices:
        result[i] = odd_values.pop(0)

    return result


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function, which takes a list `l` as input and returns a new list `l'` according to the problem description. The script then tests this function with two examples.