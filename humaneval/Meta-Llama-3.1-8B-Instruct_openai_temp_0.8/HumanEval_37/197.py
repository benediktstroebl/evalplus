```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The output list with even indices sorted
    """
    # Separate the elements at even and odd indices
    even = [x for i, x in enumerate(l) if i % 2 == 0]
    odd = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the elements at even indices
    sorted_even = sorted(even)
    
    # Combine the elements at even and odd indices
    result = []
    even_index = 0
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(sorted_even[even_index])
            even_index += 1
        else:
            result.append(x)
    
    return result

# Example usage:
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function, which takes a list `l` as input and returns a new list where the elements at even indices are sorted. The example usage demonstrates the function's behavior with two test cases.