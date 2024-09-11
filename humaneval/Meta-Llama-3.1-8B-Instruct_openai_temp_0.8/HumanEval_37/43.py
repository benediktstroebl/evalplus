### Sort Even Indices Function

```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): Input list.

    Returns:
        list: Modified list with even indices sorted.
    """
    # Separate odd and even indices
    odd_indices = [x for x in enumerate(l) if x[0] % 2!= 0]
    even_indices = [x for x in enumerate(l) if x[0] % 2 == 0]

    # Get values at even indices
    even_values = [x[1] for x in even_indices]

    # Sort the even values
    sorted_even_values = sorted(even_values)

    # Create the new list with even indices sorted
    sorted_l = [l[x[0]] if x[0] % 2!= 0 else sorted_even_values[i] for i, x in enumerate(enumerate(l))]

    return sorted_l

# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list as input and returns a new list where the even indices are sorted. The function uses list comprehensions to separate the odd and even indices, sort the even values, and then create the new list with even indices sorted. The test cases are included to demonstrate the function's behavior.