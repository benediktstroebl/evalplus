### Python Script to Sort Even Indices of a List
```markdown
### Code
```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    
    sorted_list = [val if i % 2!= 0 else even_indices[i // 2] for i, val in enumerate(l)]
    
    return sorted_list

### Test the function
if __name__ == "__main__":
    print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
    print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```
### Explanation

This script defines a function `sort_even` that takes a list `l` as input. It first creates a list of values at even indices and sorts this list. Then, it uses a list comprehension to create a new list where the values at even indices are replaced with the sorted values from the list of even indices. The function returns this new list.

The script also includes a test section at the end to verify that the function works correctly.