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
    # Separate the even and odd indices
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2!= 0]

    # Sort the elements at even indices
    even_elements = sorted([l[i] for i in even_indices])

    # Create the output list with sorted even elements at even indices
    result = [l[i] if i % 2!= 0 else even_elements[i // 2] for i in range(len(l))]

    return result


# Test the function
print(sort_even([1, 2, 3]))
# Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))
# Output: [3, 6, 5, 4]
```

This script defines the `sort_even` function, which sorts the elements at even indices in the input list while keeping the odd indices unchanged. It uses list comprehensions to separate the even and odd indices, sort the even elements, and create the output list. The function is then tested with the provided example inputs.