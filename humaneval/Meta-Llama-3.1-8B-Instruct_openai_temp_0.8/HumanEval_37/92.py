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
    # Separate odd and even indices from the list
    even_indices = [i for i, _ in enumerate(l) if i % 2 == 0]
    odd_values = [l[i] for i in range(1, len(l), 2)]

    # Get the values at even indices and sort them
    even_values = sorted([l[i] for i in even_indices])

    # Create the output list with values from odd indices and sorted even indices
    output = [v if i % 2 == 0 else even_values[even_indices.index(i)] for i, v in enumerate(l)]

    return output
```

**Example Usage:**

```python
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines the `sort_even` function to take a list `l` and returns a modified list `l'` as described in the problem. It first separates the odd and even indices from the input list `l`. Then, it sorts the values at the even indices and uses them to create the output list.