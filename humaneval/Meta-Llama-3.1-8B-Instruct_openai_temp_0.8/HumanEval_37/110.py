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
    # Separate the even and odd indexed elements
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]
    
    # Sort the even elements
    even.sort()
    
    # Combine the sorted even elements with the odd elements
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even.pop(0)
        else:
            result[i] = odd.pop(0)
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list `l` and returns a new list with the even indexed elements sorted. It uses list comprehension to separate the even and odd indexed elements, sorts the even elements, and then combines them with the odd elements in the correct order. The test cases at the end demonstrate the function's correctness.