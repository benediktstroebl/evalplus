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
    # Separate the list into odd and even indexed elements
    odd = l[1::2]
    even = l[::2]
    
    # Sort the even indexed elements
    sorted_even = sorted(even)
    
    # Replace the even indexed elements with the sorted ones
    new_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            new_list.append(sorted_even[i // 2])
        else:
            new_list.append(odd[i // 2])
    
    return new_list

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script first separates the input list into two lists: one with odd indexed elements and one with even indexed elements. It then sorts the even indexed elements. Finally, it replaces the even indexed elements in the input list with the sorted ones, while keeping the odd indexed elements the same. The result is a new list where the even indexed elements are sorted, but the odd indexed elements remain the same.