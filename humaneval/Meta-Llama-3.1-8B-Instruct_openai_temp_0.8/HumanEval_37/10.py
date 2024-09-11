```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): A list of elements to be sorted.

    Returns:
        list: A list with the even indices sorted.
    """
    # Separate the list into two lists, one for odd indices and one for even indices
    odd = [num for i, num in enumerate(l) if i % 2]
    even = [num for i, num in enumerate(l) if i % 2 == 0]
    
    # Sort the list for even indices
    even.sort()
    
    # Combine the lists, placing the even indices in their sorted order
    return [num for i, num in enumerate(odd + even) if i % 2] + even

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` as input, separates the list into two lists for odd and even indices, sorts the list for even indices, and combines the lists, placing the even indices in their sorted order. The script then tests the function with the provided examples.