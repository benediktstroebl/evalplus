```markdown
### Even Index Sorting Function

This function sorts the values at even indices of a given list while keeping the values at odd indices unchanged.

#### Code

```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.
    """
    # Separate the values at even and odd indices
    even_values = [value for i, value in enumerate(l) if i % 2 == 0]
    odd_values = [value for i, value in enumerate(l) if i % 2!= 0]

    # Sort the values at even indices
    even_values.sort()

    # Combine the sorted even values with the odd values
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_values[i // 2])
        else:
            result.append(odd_values[i // 2])

    return result

### Example Usage

print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

#### Notes

This script uses list comprehensions to separate the values at even and odd indices. It then sorts the even values and combines them with the odd values to form the final result.
```