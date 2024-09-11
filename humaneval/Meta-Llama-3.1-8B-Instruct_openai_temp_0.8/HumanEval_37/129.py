### Python Script: Sort Even Indices
```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list by even indices.
    """
    # Separate even and odd indices
    even_index_values = [l[i] for i in range(0, len(l), 2)]
    odd_index_values = [l[i] for i in range(1, len(l), 2)]

    # Sort the even index values
    even_index_values.sort()

    # Merge the sorted even index values with the odd index values
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_index_values[i // 2])
        else:
            result.append(odd_index_values[i // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```
This script defines the `sort_even` function, which separates the input list into even and odd index values, sorts the even index values, and then merges them back with the odd index values to produce the final sorted list. The test cases at the end demonstrate the function's correctness.