```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the odd and even indices
    odd = [l[i] for i in range(len(l)) if i % 2 == 0]
    even = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort the even elements
    even.sort()

    # Combine the sorted even elements with the odd elements
    result = []
    for i in range(len(l)):
        if i % 2 == 0:  # If the index is even
            result.append(even.pop(0))
        else:  # If the index is odd
            result.append(odd.pop(0))

    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script uses list comprehension to separate the elements at odd and even indices, sorts the even elements, and then combines them in the correct order. The `pop(0)` method is used to remove and return the first element of the list, which ensures that the elements are processed in the correct order. The function returns the modified list.