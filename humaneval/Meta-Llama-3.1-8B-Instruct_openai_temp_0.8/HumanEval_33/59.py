```python
def sort_third(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, 
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(l) if j % 3 == 0])[k // 3] 
            for i, x in enumerate(l) for k in range(i % 3)]
    
# Test the function
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script uses a list comprehension to iterate over both the elements of the list and their indices. It then uses another list comprehension to iterate over the elements at indices divisible by three, sorts them, and takes the corresponding element from the sorted list for the current index. The `enumerate` function is used to get both the index and the value of each element in the list. The `//` operator is used for integer division, since we want to divide the current index by 3 to get the index of the corresponding element in the sorted list.