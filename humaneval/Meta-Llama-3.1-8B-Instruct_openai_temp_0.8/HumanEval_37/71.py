```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indicies sorted.
    """
    # Separate the odd and even indices
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]
    even = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    
    # Combine the odd and sorted even indices
    return [even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(l))]

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` and returns a new list with even indices sorted. It uses list comprehensions to separate the odd and even indices, and then combines them back together, replacing the even indices with their sorted values. The test cases at the end demonstrate the function's behavior with two examples.