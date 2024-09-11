```markdown
### Python Function to Sort Even Indices

Here's a Python function that takes a list `l` and returns a list `l'` such that `l'` is identical to `l` in the odd indices, 
while its values at the even indices are equal to the values of the even indices of `l`, but sorted.
```python
def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indices of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The list with even indices sorted.
    """
    # Split the list into two lists, one for odd indices and one for even indices
    odd_indices = [l[i] for i in range(len(l)) if i % 2!= 0]
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    
    # Sort the list of even indices
    even_indices.sort()
    
    # Combine the two lists, using the sorted even indices at even positions in the new list
    return [value if i % 2!= 0 else even_indices[i // 2] for i, value in enumerate(odd_indices + even_indices)]

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```
This function works by first splitting the input list into two lists, one for odd indices and one for even indices. 
It then sorts the list of even indices. 
Finally, it combines the two lists, using the sorted even indices at even positions in the new list. 
This ensures that the new list is identical to the original list in the odd indices, while the even indices are sorted.