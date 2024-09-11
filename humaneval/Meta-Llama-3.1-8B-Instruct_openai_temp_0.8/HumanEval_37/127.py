Here's a Python script that solves the problem:

```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indices sorted.
    """
    # Separate even and odd indices
    even = [i for i, x in enumerate(l) if i % 2 == 0]
    odd = [i for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the values at even indices
    sorted_even = sorted([l[i] for i in even])
    
    # Combine the results
    sorted_l = [l[i] if i % 2!= 0 else sorted_even.pop(0) for i in range(len(l))]
    
    return sorted_l

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script uses list comprehensions to separate the even and odd indices, sorts the values at even indices, and then combines the results to produce the final sorted list.