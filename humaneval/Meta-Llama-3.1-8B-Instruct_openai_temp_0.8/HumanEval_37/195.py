### even_sort.py
```markdown
### even_sort function

This function sorts the values at even indices in a given list,
while keeping the values at odd indices unchanged.

#### Args:
* `l` (list): The input list.

#### Returns:
* `list`: The modified list with even index values sorted.
```python
def sort_even(l: list):
    """sort_even function

    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate even and odd indices
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2!= 0]
    
    # Sort values at even indices
    even_values = sorted([l[i] for i in even_indices])
    
    # Create the output list
    output = [None] * len(l)
    for i in even_indices:
        output[i] = even_values.pop(0)
    for i in odd_indices:
        output[i] = l[i]
    
    return output

# Example usage
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function and provides example usage of the function. It separates the input list into even and odd indices, sorts the values at even indices, and then constructs the output list by combining the sorted even values with the original odd values.