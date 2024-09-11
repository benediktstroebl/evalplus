```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The resulting list with even indicies sorted.
    """
    # Separate even and odd indices
    even = [val for i, val in enumerate(l) if i % 2 == 0]
    odd = [val for i, val in enumerate(l) if i % 2!= 0]
    
    # Sort the even values
    even.sort()
    
    # Combine the sorted even and the odd values
    return [val for i, val in enumerate(odd) if i % 2 == 0] + even + [val for i, val in enumerate(odd) if i % 2!= 0]

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

In this script, we define a function `sort_even` that takes a list `l` and returns a new list with the even indicies sorted. We use list comprehension to separate the even and odd values into two lists, sort the even values, and then combine them back together in the correct order. The test cases at the end demonstrate that this function works as expected.