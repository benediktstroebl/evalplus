```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem description.
    """
    # Separate odd and even indices
    odd = [x for i, x in enumerate(l) if i % 2 == 0]
    even = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even indices
    even.sort()
    
    # Combine the odd and sorted even indices back into the original order
    result = []
    odd_index = 0
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            # Insert the even index at its correct position
            result.insert(i, even[even_index])
            even_index += 1
        else:
            # Insert the odd index at its correct position
            result.insert(i, odd[odd_index])
            odd_index += 1
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function as per the problem description, which takes a list `l` and returns a new list where the elements at even indices are sorted. The script then tests this function with the given examples.