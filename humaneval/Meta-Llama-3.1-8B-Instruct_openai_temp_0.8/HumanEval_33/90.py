```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Use list comprehension to create a new list that is identical to l
    # for indices that are not divisible by three
    l_prime = [x for i, x in enumerate(l) if i % 3!= 0]
    
    # Find the indices of l that are divisible by three
    to_sort = [i for i in range(len(l)) if i % 3 == 0]
    
    # Sort the values at these indices
    sorted_values = sorted([l[i] for i in to_sort])
    
    # Replace the values in l_prime at the indices of to_sort with
    # the sorted values
    for i in to_sort:
        l_prime.insert(i, sorted_values.pop(0))
    
    return l_prime

# Test the function
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script defines a function `sort_third` that takes a list `l` as input and returns a new list `l'` according to the problem description. The function uses list comprehensions and indexing to create the new list, and the `sorted` function to sort the values at the specified indices. The function is then tested with the provided example inputs.