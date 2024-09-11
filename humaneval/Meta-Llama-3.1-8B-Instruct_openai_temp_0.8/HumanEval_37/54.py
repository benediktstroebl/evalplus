```markdown
### Even Index Sort Function

#### Description

This function takes a list and returns a new list where values at even indices are sorted.
Values at odd indices are left unchanged.

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
        list: The new list with even indices sorted.
    """
    # Separate even and odd indexed elements into different lists
    even_idx_elements = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd_idx_elements = [l[i] for i in range(len(l)) if i % 2 == 1]

    # Sort even indexed elements
    even_idx_elements.sort()

    # Combine the sorted even indexed elements with odd indexed elements
    sorted_list = []
    for i in range(len(even_idx_elements)):
        sorted_list.append(even_idx_elements[i])
        sorted_list.append(odd_idx_elements[i])

    return sorted_list

# Example usage
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

#### Example Output

```
[1, 2, 3]
[3, 6, 5, 4]
```
```