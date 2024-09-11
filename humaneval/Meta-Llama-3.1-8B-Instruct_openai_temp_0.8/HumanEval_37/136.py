```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list.
    """
    # Separate the elements at odd and even indices
    odd = l[1::2]
    even = l[::2]
    
    # Sort the elements at even indices
    even.sort()
    
    # Combine the sorted even elements with the odd elements to form the result
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even[i // 2]
        else:
            result[i] = odd[i // 2]
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```