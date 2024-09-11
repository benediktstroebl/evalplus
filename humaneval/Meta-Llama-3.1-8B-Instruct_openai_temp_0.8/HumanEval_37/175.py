```markdown
### Even Indexed Sorting Function

This script defines a function `sort_even` that takes a list and returns a new list
where the values at even indices are sorted, but the values at odd indices remain the same.

#### Code

```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The output list with even indices sorted
    """
    # Separate the even and odd indices
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2!= 0]

    # Split the list into two lists at the even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]

    # Sort the even values
    even_values.sort()

    # Combine the sorted even values and the odd values back into a list
    result = [None] * len(l)
    for i, value in enumerate(even_values):
        result[even_indices[i]] = value
    for i, value in enumerate(odd_values):
        result[odd_indices[i]] = value

    return result

# Example use cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

#### Explanation

This function works by first separating the even and odd indices of the input list.
It then splits the list into two lists at the even and odd indices.
The even values are sorted, and the sorted even values and the odd values are combined back into a list.
The result is a list where the values at even indices are sorted, but the values at odd indices remain the same.
```