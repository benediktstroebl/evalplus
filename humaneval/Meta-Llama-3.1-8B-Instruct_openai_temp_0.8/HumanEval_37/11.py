```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list
    
    Returns:
        list: The sorted list according to the problem description
    """
    even_values = sorted([x for i, x in enumerate(l) if i % 2 == 0])  # Get even indexed values and sort them
    return [x if i % 2!= 0 else even_values[i // 2] for i, x in enumerate(l)]  # Alternate between original and sorted values

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script uses list comprehension to iterate over the input list `l`. If the index `i` is even, it adds the corresponding value from `l` to the `even_values` list, which is then sorted. If the index `i` is odd, it keeps the original value from `l`. The resulting list is then returned.