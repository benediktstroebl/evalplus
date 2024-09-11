**Sorting a List at Indices Divisible by Three**
=====================================================

Here is a Python script that solves the problem:

```python
def sort_third(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three,
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Separate the list into two lists: one for indices that are divisible by 3 and one for the rest
    div_by_three = [x for i, x in enumerate(l) if i % 3 == 0]
    not_div_by_three = [x for i, x in enumerate(l) if i % 3!= 0]
    
    # Sort the list for indices that are divisible by 3
    div_by_three.sort()
    
    # Combine the two lists back together, using the sorted list for indices that are divisible by 3
    result = [None] * len(l)
    for i, (x, y) in enumerate(zip(not_div_by_three, l)):
        result[i] = x
    for i, x in enumerate(div_by_three):
        result[i] = x
    
    return result

# Test the function
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script uses list comprehensions to separate the input list into two lists: one for indices that are divisible by 3 and one for the rest. It then sorts the list for indices that are divisible by 3. The two lists are combined back together to form the final result, with the values for indices that are divisible by 3 being taken from the sorted list.