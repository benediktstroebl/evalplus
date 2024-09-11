```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l (list): The input list
    
    Returns:
        list: A sorted list of unique elements
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    unique_list = sorted(list(unique_set))
    
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, I've used the following steps to solve the problem:

1.  I've defined a function `unique` that takes a list `l` as input.
2.  Inside the function, I've converted the list to a set `unique_set` using the `set()` function. This removes all duplicate elements in the list because sets in Python cannot contain duplicate values.
3.  I've then converted the set back to a list `unique_list` using the `list()` function and sorted it using the `sorted()` function.
4.  Finally, I've returned the sorted list of unique elements.
5.  I've also included a test case at the end to demonstrate the usage of the function.