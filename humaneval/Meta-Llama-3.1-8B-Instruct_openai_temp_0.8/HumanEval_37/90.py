```markdown
### Sort Even Indices Function

This function takes a list `l` and returns a list `l'` such that
`l'` is identical to `l` in the odd indices, while its values at the even indices are equal
to the values of the even indices of `l`, but sorted.

#### Code

```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.
    """
    # Separate even and odd indices values
    even_values = [l[i] for i in range(0, len(l), 2)]
    odd_values = [l[i] for i in range(1, len(l), 2)]

    # Sort the even indices values
    even_values.sort()

    # Combine even and odd indices values
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_values[i // 2])
        else:
            result.append(odd_values[i // 2])

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

#### Output

```
[1, 2, 3]
[3, 6, 5, 4]
```